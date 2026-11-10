# ==========================================
# DOWNHOLE TELEMETRY CALCULATION
# ==========================================

# Activity B: Define variables

well_id = "WELL-07"

# Store sensor readings as strings first
pressure_psi_raw = "3150.0"
temperature_f_raw = "186.0"

sensor_active = True

# Convert strings into floating-point numbers
pressure_psi = float(pressure_psi_raw)
temperature_f = float(temperature_f_raw)

# Activity C: Perform unit conversions

pressure_kpa = pressure_psi * 6.8947572932

temperature_c = (temperature_f - 32) * 5 / 9

# Activity D: Generate a formatted report

print("========== DOWNHOLE TELEMETRY REPORT ==========")

print(f"Well ID: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor Status: {'Active' if sensor_active else 'Inactive'}")

print("===============================================")
