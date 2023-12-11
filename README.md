# RainfallRecords

## Overview

This Python program manages and analyzes rainfall records for different cities. It consists of several classes and functions designed to handle operations such as viewing, editing, deleting, and adding rainfall records. The main features include:

- **Classes:**
  - `RainfallRecord`: Represents a single record of rainfall information, including sun hours, average rainfall, value, minimum and maximum temperatures, and year.
  - `Driver`: Manages an assortment of `RainfallRecord` instances and provides a method to read data from a CSV file.
  - `Archive`: Represents an archive of rainfall records for a specific city, offering operations for adding, removing, and calculating a basic moving average.

- **Functions:**
  - `return_driver(file_name)`: Reads data from the specified CSV file to create and return a `Driver` instance.
  - `rainfall(year, city)`: Asks the user to select a month and returns the amount of rainfall for that month in the specified year and city.
  - `average_rainfall(year, city)`: Asks the user to select months and computes the average rainfall for those months within the entered year and city.
  - `delete(year, city, city_name)`: Deletes the rainfall record for a specified month in the given year and city.
  - `insert(year, city, city_name)`: Adds a new rainfall record for a specified month and year.

## Usage

1. **Installation:**
   - Clone the repository: `git clone https://github.com/your-username/your-repository.git`
   - Navigate to the project directory: `cd your-repository`

2. **Run the Program:**
   - Execute the main script: `python main.py`

3. **Interact with the Program:**
   - Enter the desired city and year when prompted.
   - Choose from the menu of options to perform various operations related to rainfall records.

## Notes

- The program assumes that rainfall data is stored in CSV files with city names appended to them, such as "Oxford.csv".
- The `Archive` class provides additional capabilities for archiving records and calculating a basic moving average.
- The user interacts with the program through a text-based interface by entering corresponding numbers.

