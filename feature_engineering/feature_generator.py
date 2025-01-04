import pandas as pd
from sklearn.preprocessing import StandardScaler
from utils.logger import get_logger

logger = get_logger("FeatureGenerator")

def generate_features(data):
    """
    Generates engineered features for machine learning models.
    """
    try:
        # Example feature: Moving Average
        data["7_day_moving_avg"] = data["sales"].rolling(window=7).mean()
        
        # Normalize price
        scaler = StandardScaler()
        data["normalized_price"] = scaler.fit_transform(data[["price"]])
        
        logger.info("Feature generation completed.")
        return data
    except Exception as e:
        logger.error(f"Error in feature generation: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    sample_data = pd.DataFrame({
        "sales": [100, 200, 150, 300, 250, 400, 350],
        "price": [20, 21, 19, 22, 23, 24, 25]
    })
    processed_data = generate_features(sample_data)
    print(processed_data)
