import unittest
from flask import Flask
from api.routes import api_blueprint

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(api_blueprint)
        self.client = self.app.test_client()

    def test_health_check(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json)

    def test_predict_demand(self):
        data = {"features": [1, 2, 3]}
        response = self.client.post("/api/predict-demand", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json)

if __name__ == "__main__":
    unittest.main()
