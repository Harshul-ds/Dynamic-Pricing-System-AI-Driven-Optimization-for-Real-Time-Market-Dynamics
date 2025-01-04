import joblib
import os

def save_model(model, file_path):
    """
    Saves a trained model to the specified file path.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        joblib.dump(model, file_path)
        print(f"Model saved at {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error saving model: {str(e)}")

def load_model(file_path):
    """
    Loads a trained model from the specified file path.
    """
    try:
        model = joblib.load(file_path)
        print(f"Model loaded from {file_path}")
        return model
    except Exception as e:
        raise RuntimeError(f"Error loading model: {str(e)}")
