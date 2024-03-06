import pandas as pd
import json


class CarAnalyzer:
    def __init__(self, filename='cars.json'):
        self.filename = filename
        self.data = None

    def load_data_from_json(self, filename):
        try:
            with open(filename, 'r') as f:
                loaded_json = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {filename}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON file")
        
        self.data = pd.DataFrame(loaded_json)

    def get_unique_car_count(self):
        if self.data is None:
            raise RuntimeError("Data is not loaded. Please call load_data_from_json() first.")
        df_without_duplicates = self.data.drop_duplicates()
        return print(len(df_without_duplicates))

    def get_avegage_horsepower(self):
        # TODO:     Print the average horse power of all the cars.
        return


    def get_top_five_heaviest_cars(self):
        # TODO:    Print the top 5 most heaviest cars.
        return


    def get_cars_count_by_manifacturer(self):
        # TODO:     Print the number of cars made by each manufacturer.
        return

    
    def get_cars_count_per_year(self):
        # TODO:     Print the number of cars made each year.
        return


    def save_data_to_csv(self):
        # TODO:     Save the dataset to a CSV file.
        return



analyzer = CarAnalyzer()
analyzer.load_data_from_json("D:\\dev\\cars\\cars.json")
analyzer.get_unique_car_count()