"""Week 9 Class 5: complete the TODOs; do not import instructor solutions."""
import csv
from pathlib import Path

PSI_TO_KPA = 6.8947572932


def convert_pressure(value, unit):
    """Return pressure in kPa; reject unsupported units."""
    if unit == "psi":
        pressure_kpa = value * PSI_TO_KPA
    elif unit == "kPa":
        pressure_kpa = value
    else:
        raise ValueError(f"Unsupported pressure unit: {unit}")

    return pressure_kpa


def convert_temperature(value, unit):
    """Return temperature in degrees Celsius."""
    if unit == "F":
        temperature_c = (value - 32) * 5 / 9
    elif unit == "C":
        temperature_c = value
    else:
        raise ValueError(f"Unsupported temperature unit: {unit}")

    return temperature_c


def parse_record(raw_line):
    """Return normalized dictionary; raise ValueError for malformed records."""
    fields = [field.strip() for field in raw_line.strip().split("|")]

    if len(fields) != 7:
        raise ValueError("Expected exactly seven fields")

    if not all(fields):
        raise ValueError("Fields must not be empty")

    well_id, timestamp, pressure_text, pressure_unit, temperature_text, temperature_unit, status = fields

    try:
        pressure = float(pressure_text)
        temperature = float(temperature_text)
    except ValueError:
        raise ValueError("Invalid numeric value")

    if pressure < 0:
        raise ValueError("Pressure must be non-negative")

    status = status.upper()

    if status not in ["ACTIVE", "INACTIVE", "PAUSED"]:
        raise ValueError("Unsupported status: " + status)

    return {
        "well_id": well_id,
        "timestamp": timestamp,
        "pressure_kpa": round(convert_pressure(pressure, pressure_unit), 2),
        "temperature_c": round(convert_temperature(temperature, temperature_unit), 2),
        "status": status,
    }


def process_lines(lines):
    """Return (accepted_records, rejected_records) preserving source line numbers."""
    accepted_records = []
    rejected_records = []

    for line_number, raw_line in enumerate(lines, start=1):
        if not raw_line.strip() or raw_line.strip().startswith("#"):
            continue

        try:
            record = parse_record(raw_line)
            accepted_records.append(record)

        except ValueError as error:
            rejected_records.append({
                "line_number": line_number,
                "raw_line": raw_line.strip(),
                "error": str(error),
            })

    return accepted_records, rejected_records


def summarize_by_well(records):
    """Average pressure for ACTIVE records, sorted by well ID."""
    well_pressures = {}

    for record in records:
        if record["status"] == "ACTIVE":
            well_id = record["well_id"]
            pressure = record["pressure_kpa"]

            if well_id not in well_pressures:
                well_pressures[well_id] = []

            well_pressures[well_id].append(pressure)

    summary = []

    for well_id in sorted(well_pressures):
        pressures = well_pressures[well_id]
        average_pressure = sum(pressures) / len(pressures)

        summary.append({
            "well_id": well_id,
            "average_pressure_kpa": round(average_pressure, 2),
            "record_count": len(pressures),
        })

    return summary


def write_csv(path, fieldnames, records):
    """Create output CSV with a header row."""
    with open(path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def run(input_path, output_dir):
    """Generate cleaned_telemetry.csv, rejected_records.csv, well_summary.csv."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    accepted_records, rejected_records = process_lines(lines)

    summary = summarize_by_well(accepted_records)

    write_csv(
        output_dir / "cleaned_telemetry.csv",
        ["well_id", "timestamp", "pressure_kpa", "temperature_c", "status"],
        accepted_records,
    )

    write_csv(
        output_dir / "rejected_records.csv",
        ["line_number", "raw_line", "error"],
        rejected_records,
    )

    write_csv(
        output_dir / "well_summary.csv",
        ["well_id", "average_pressure_kpa", "record_count"],
        summary,
    )

    print("Capstone processing completed.")
    print("Accepted records:", len(accepted_records))
    print("Rejected records:", len(rejected_records))
    print("Output folder:", output_dir)


if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_folder = input("Enter the output folder name: ")

    run(input_file, output_folder)