import json
import pandas as pd
import yaml


# Read settings from config.yml
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

max_days = config["max_days_since_calibration"]
output_file = config["output_file"]


# Read sensor and calibration data
sensors = pd.read_excel("sensors.xlsx")
calibrations = pd.read_csv("calibrations.csv")


# Join the sensor information with calibration information
data = pd.merge(
    sensors,
    calibrations,
    on="sensor_id"
)


# Find overdue sensors
overdue = data[
    data["days_since_calibration"] > max_days
]


# Select the information required in the JSON file
result = overdue[
    ["sensor_id", "lab_room", "owner", "days_since_calibration"]
]


# Convert to a list of dictionaries
result = result.to_dict(orient="records")


# Write the overdue sensors to JSON
with open(output_file, "w") as file:
    json.dump(result, file, indent=2)


print(f"Overdue sensors written to {output_file}")
