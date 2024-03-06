import pandas as pd
import json


class CarAnalyzer:
    """
    Analyzes car data loaded from a JSON file.

    Attributes:
        data (pd.DataFrame, optional): DataFrame containing the loaded car data. None initially.
    """
    def __init__(self):
        """
        Initializes the CarAnalyzer object. The data attribute is initially set to None.
        """
        self.data = None

    def load_data_from_json(self, filename):
        """
        Loads car data from a JSON file into a pandas DataFrame.

        Args:
            filename (str): Path to the JSON file containing car data.

        Raises:
            FileNotFoundError: If the specified JSON file is not found.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        try:
            with open(filename, 'r') as f:
                loaded_json = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {filename}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON file")
        
        self.data = pd.DataFrame(loaded_json)

    def get_unique_car_count(self):
        """
        Returns the number of unique cars in the loaded data.

        Raises:
            RuntimeError: If data is not loaded.
        """
        if self.data is None:
            raise RuntimeError("Data is not loaded. Please call load_data_from_json() first.")
        df_without_duplicates = self.data.drop_duplicates()
        return print(f"Unique cars count: {len(df_without_duplicates)}")

    def get_avegage_horsepower(self):
        """
        Returns the average horsepower of all cars in the loaded data.

        Raises:
            RuntimeError: If data is not loaded.
            KeyError: If the "horsepower" column is not found in the data.
        """
        if self.data is None:
            raise RuntimeError("Data is not loaded. Please call load_data_from_json() first.")
        try:
            return print(f"Average horsepower: {str(round(self.data['horsepower'].mean(), 2))}")
        except KeyError:
            raise KeyError('Horsepower column not found in dataset')


    def get_top_five_heaviest_cars(self):
        """
        Returns the top 5 heaviest cars (by weight) in the loaded data as a DataFrame.

        Raises:
            RuntimeError: If data is not loaded.
            KeyError: If the "weight" column is not found in the data.
        """
        if self.data is None:
            raise RuntimeError("Data is not loaded. Please call load_data_from_json() first.")

        try:
            return print(f"Top 5 heaviest cars:\n {self.data.nlargest(5, "weight")}")
        except KeyError:
            raise KeyError('Weight column not found in dataset')

    def get_cars_count_by_manifacturer(self):
        """
        Returns the number of cars made by each manufacturer in the loaded data as a Series.

        Raises:
            RuntimeError: If data is not loaded.
        """
        if self.data is None:
            raise RuntimeError("Data is not loaded. Please call load_data_from_json() first.")
         
        return print(f"Cars count by manifacturer:\n {self.data["make"].value_counts()}")

    
    def get_cars_count_per_year(self):
        """
        Returns the number of cars made each year in the loaded data as a Series.

        Raises:
            RuntimeError: If data is not loaded.
        """
        if self.data is None:
            raise RuntimeError("Data is not loaded. Please call load_data_from_json() first.")
         
        return print(f"Cars count per year:\n {self.data["year"].value_counts()}")

    def save_data_to_csv(self, output_file='cars.csv'):
        """
        Saves the loaded car data to a CSV file.

        Args:
            output_file (str, optional): Name of the output CSV file. Defaults to 'cars.csv'.

        Raises:
            RuntimeError: If data is not loaded.
        """
        if self.data is None:
            raise RuntimeError("Data is not loaded. Please call load_data_from_json() first.")
        
        return self.data.to_csv(output_file, sep=",", index=False, encoding="utf-8")