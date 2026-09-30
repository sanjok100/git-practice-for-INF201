# INF201 Week 40 Exercises

This repository contains my solutions for the **INF201 Week 40 exercises**.

## Task 1 – GitHub Repository

The first task was to practice using Git and GitHub by creating a repository, cloning it using VS Code, and pushing a Python file.

The repository includes:

* `hello.py` – a simple Python program that prints:

```text
Hello, World
```

## Task 2 – Working with Multiple Formats

The second task is a Python script for checking laboratory equipment calibration status.

The script:

1. Reads calibration settings from a YAML file.
2. Reads sensor information from an Excel file.
3. Reads calibration data from a CSV file.
4. Matches the sensor and calibration information.
5. Identifies sensors whose calibration is overdue.
6. Exports the overdue sensors to a formatted JSON file.

### Files

* `week40_exercise.py` – Python script for the exercise.
* `config.yml` – Configuration settings.
* `sensors.xlsx` – Sensor information.
* `calibrations.csv` – Calibration information.
* `overdue_sensors.json` – Generated JSON output.
* `hello.py` – Task 1 Git practice file.

### Requirements

The following Python packages are required:

```bash
pip install pandas openpyxl pyyaml
```


The program after executing reads the input files and creates the JSON output file specified in `config.yml`.


