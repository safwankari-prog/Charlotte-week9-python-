
# WEEK 9 - CLASS 1 HOMEWORK
# Question 9: Engineering Unit Conversions

# Step 1: Define variables
well_id = "WELL-07"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

# Step 2: Convert pressure from psi to kPa
pressure_kpa = pressure_psi * 6.8947572932

# Step 3: Convert temperature from Fahrenheit to Celsius
temperature_c = (temperature_f - 32) * 5 / 9

# Step 4: Display the report
print("========== DOWNHOLE TELEMETRY REPORT ==========")
print(f"Well ID: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor Status: {'Active' if sensor_active else 'Inactive'}")
print("================================================")


# Question 11: Demonstrating a type mismatch

raw_pressure = "3150"

# This line intentionally causes a TypeError
# pressure_kpa = raw_pressure * 6.8947572932

# Convert string into a float
pressure_psi = float(raw_pressure)

# Perform the calculation
pressure_kpa = pressure_psi * 6.8947572932

print(f"Pressure: {pressure_kpa:.1f} kPa")
