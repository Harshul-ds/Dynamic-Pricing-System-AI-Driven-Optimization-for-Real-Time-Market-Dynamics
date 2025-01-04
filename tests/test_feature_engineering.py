import unittest
import pandas as pd
from feature_engineering.feature_generator import generate_features

class TestFeatureEngineering(unittest.TestCase):
    def test_generate_features(self):
        sample_data = pd.DataFrame({"sales": [100, 200, 300], "price": [20, 21, 19]})
        processed_data = generate_features(sample_data)
        self.assertIn("7_day_moving_avg", processed_data.columns)

if __name__ == "__main__":
    unittest.main()
