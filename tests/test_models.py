import unittest
from models.price_elasticity import compute_price_elasticity
from models.rl_optimizer import train_rl_model, predict_optimal_price

class TestModels(unittest.TestCase):
    def test_price_elasticity(self):
        prices = [10, 15, 20, 25, 30]
        demands = [100, 80, 60, 40, 20]
        result = compute_price_elasticity(prices, demands)
        self.assertIn("price_elasticity", result)
        self.assertLess(result["mse"], 1000)

    def test_rl_optimizer(self):
        env_name = "CartPole-v1"  # Replace with a pricing-specific environment
        model = train_rl_model(env_name, timesteps=1000)
        observation = [0.5, 0.2]  # Replace with real features
        optimal_price = predict_optimal_price(model, observation)
        self.assertIsNotNone(optimal_price)

if __name__ == "__main__":
    unittest.main()
