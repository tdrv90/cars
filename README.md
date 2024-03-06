# Car Analyzer

This Python project provides a versatile CarAnalyzer class to analyze car data loaded from a JSON file.

## Features

- **Data Loading**: Loads car data from JSON files.
- **Unique Car Count**: Calculates the number of distinct cars in the dataset.
- **Average Horsepower**: Computes the average horsepower of all cars.
- **Top 5 Heaviest Cars**: Identifies the top 5 heaviest cars based on the "weight" column.
- **Car Count by Manufacturer**: Counts the number of cars manufactured by each brand.
- **Car Count per Year**: Counts the number of cars manufactured each year.
- **CSV Export**: Saves the loaded car data to a CSV file for further analysis.


## Installation

To install this package, run the following command in your terminal:

`python setup.py bdist_wheel sdist`

`pip install .`

## Usage

1. Import the CarAnalyzer class:

`from carsanalyzer import CarAnalyzer`

2. Create an instance of CarAnalyzer:

`analyzer = CarAnalyzer()`

3. Call the desired methods to analyze the data:


`load_data_from_json()`: Loads the JSON file

`get_unique_car_count()`: Returns the number of unique cars.

`get_average_horsepower()`: Returns the average horsepower.

`get_top_five_heaviest_cars()`: Returns a DataFrame of the top 5 heaviest cars.

`get_cars_count_by_manifacturer()`: Returns a Series count of cars by manufacturer.

`get_cars_count_per_year()`: Returns a Series count of cars made each year.

`save_data_to_csv(output_file="analyzed_cars.csv")`: Saves the data to a CSV file (optional, default output "analyzed_cars.csv").


## Dependencies

This project requires the following Python libraries:

pandas