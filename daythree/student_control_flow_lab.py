"""Charlotte Projects | Week 9 Class 3 student lab. Standard library only."""

# The data is supplied as Python dictionaries so file parsing can wait until Class 4.
READINGS = [
    {"well_id": "WELL-07", "pressure_psi": 3150.0, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2780.0, "status": "active"},
    {"well_id": "WELL-09", "pressure_psi": 3325.0, "status": "inactive"},
    {"well_id": "WELL-10", "pressure_psi": 2895.0, "status": "active"},
    {"well_id": "WELL-07", "pressure_psi": 3210.0, "status": "active"},
    {"well_id": "WELL-11", "pressure_psi": None, "status": "active"},
    {"well_id": "WELL-08", "pressure_psi": 2810.0, "status": "active"},
    {"well_id": "WELL-12", "pressure_psi": 2715.0, "status": "inactive"},
    {"well_id": "WELL-10", "pressure_psi": 4100.0, "status": "active"},
    {"well_id": "WELL-13", "pressure_psi": -25.0, "status": "active"},
]

# TODO A: Write classify_pressure(pressure_psi) that returns
# "invalid" for None or negative values; "high" for >= 3500;
# "normal" for >= 2500 and < 3500; otherwise "low".
def classify_pressure(pressure_psi):

    if pressure_psi is None or pressure_psi < 0:
        return "invalid"

    elif pressure_psi >= 3500:
        return "high"

    elif pressure_psi >= 2500:
        return "normal"

    else:
        return "low"


# TODO B: Write psi_to_kpa(pressure_psi) using factor 6.8947572932.
# Return None for invalid pressures (None or negative).
def psi_to_kpa(pressure_psi):

    if pressure_psi is None or pressure_psi < 0:
        return None

    return pressure_psi * 6.8947572932

# TODO C: Loop through READINGS and report the classification for
# every observation, even if a sensor is inactive.
for reading in READINGS:

    well_id = reading["well_id"]
    pressure = reading["pressure_psi"]

    classification = classify_pressure(pressure)

    print(f"{well_id}: {classification}")


# TODO D: Use a loop with continue to calculate averages for ACTIVE,
# VALID observations only, grouped by well_id. Do not overwrite repeats.
# Use dictionaries for running totals and counts.
well_totals = {}
well_counts = {}

valid_active_count = 0
skipped_count = 0

for reading in READINGS:

    if reading["status"] != "active":
        skipped_count += 1
        continue

    pressure = reading["pressure_psi"]

    if classify_pressure(pressure) == "invalid":
        skipped_count += 1
        continue

    well_id = reading["well_id"]

    if well_id not in well_totals:
        well_totals[well_id] = 0
        well_counts[well_id] = 0

    well_totals[well_id] += pressure
    well_counts[well_id] += 1

    valid_active_count += 1

# TODO E: Print the number of valid active observations, the
# number skipped, and well averages rounded to 2 decimals.
print("\nSTUDENT CONTROL FLOW RESULTS")
print("-----------------------------")

print(f"Valid active observations: {valid_active_count}")
print(f"Skipped observations: {skipped_count}")

print("\nAverage Pressure Per Well:")

for well_id in sorted(well_totals):

    average = well_totals[well_id] / well_counts[well_id]

    print(f"{well_id}: {average:.2f} PSI")

if __name__ == "__main__":
    print("Complete the TODOs, then run this file.")

 

 


