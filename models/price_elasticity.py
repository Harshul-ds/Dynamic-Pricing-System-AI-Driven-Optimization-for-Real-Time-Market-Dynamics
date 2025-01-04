from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def compute_price_elasticity(prices, demands):
    """
    Computes price elasticity of demand using linear regression.
    """
    try:
        # Reshape data for regression
        prices = np.array(prices).reshape(-1, 1)
        demands = np.array(demands).reshape(-1, 1)

        model = LinearRegression()
        model.fit(prices, demands)

        elasticity = model.coef_[0][0]
        mse = mean_squared_error(demands, model.predict(prices))

        return {
            "price_elasticity": elasticity,
            "mse": mse,
        }
    except Exception as e:
        raise RuntimeError(f"Error in price elasticity computation: {str(e)}")

if __name__ == "__main__":
    prices = [10, 15, 20, 25, 30]
    demands = [100, 80, 60, 40, 20]
    result = compute_price_elasticity(prices, demands)
    print(result)
