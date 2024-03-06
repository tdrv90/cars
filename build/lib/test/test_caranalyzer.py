import unittest
import pandas as pd
import io
import json
from src.carsanalyzer import CarAnalyzer

class TestCarAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = CarAnalyzer()

        # Sample data:
        self.data = {
             "make": ["Honda", "Toyota", "Ford", "Honda"],
            "model": ["Civic", "Camry", "Mustang", "Accord"],
            "year": [2023, 2022, 2020, 2021],
            "horsepower": [158, 203, 310, 192],
            "weight": [1200, 1400, 1600, 950]
        }
    
    def test_load_data_from_json_success(self):
        # Create a mock file object with valid JSON data
        mock_file = io.StringIO(json.dumps(self.data))

        # Call the method with the mock file
        self.analyzer.load_data_from_json(mock_file)

        # Check if data is loaded correctly
        self.assertEqual(self.analyzer.data.shape, (4, 5))
        self.assertTrue("make" in self.analyzer.data.columns)
    
    def test_load_data_from_json_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.analyzer.load_data_from_json("non-existent_file.json")

    
    def test_load_data_from_json_invalid_json(self):
        # Create a mock file with invalid JSON data
        mock_file = io.StringIO("invalid_json_data")

        with self.assertRaises(json.JSONDecodeError):
            self.analyzer.load_data_from_json(mock_file)


    def test_get_unique_car_count(self):
        # Load sample data
        self.analyzer.data = pd.DataFrame(self.data)

        # Call the method
        unique_count = self.analyzer.get_unique_car_count()

        # Check the returned value
        self.assertEqual(unique_count, 3)


    def test_get_unique_car_count_data_not_loaded(self):
        with self.assertRaises(RuntimeError):
            self.analyzer.get_unique_car_count()   

    def test_get_average_horsepower(self):
        # Load sample data
        self.analyzer.data = pd.DataFrame(self.data)

        # Call the method
        average_hp = self.analyzer.get_average_horsepower()

        # Check the returned value (rounded to 2 decimal places)
        self.assertEqual(average_hp, 213.25)

    def test_get_average_horsepower_data_not_loaded(self):
        with self.assertRaises(RuntimeError):
            self.analyzer.get_average_horsepower()

    def test_get_average_horsepower_column_missing(self):
        # Load sample data without the "horsepower" column
        self.analyzer.data = pd.DataFrame(self.data.items(), columns=["make", "model", "year", "weight"])

        with self.assertRaises(KeyError):
            self.analyzer.get_average_horsepower()

    # TODO: similar tests to be added for the rest of the methods
            
unittest.main()