import unittest
from data_ingestion.batch_ingestion import load_batch_data

class TestDataIngestion(unittest.TestCase):
    def test_load_batch_data(self):
        file_path = "tests/sample_data.csv"
        data = load_batch_data(file_path)
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

if __name__ == "__main__":
    unittest.main()
