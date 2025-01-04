from flask import Blueprint, request, jsonify
from models.demand_forecasting import predict_demand
from utils.logger import get_logger

logger = get_logger("API-Routes")
api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/predict-demand", methods=["POST"])
def predict():
    """
    Endpoint to predict demand.
    """
    try:
        data = request.get_json()
        if not data or "features" not in data:
            return {"error": "Invalid input data"}, 400
        
        features = data["features"]
        prediction = predict_demand(features)
        return jsonify({"prediction": prediction}), 200
    except Exception as e:
        logger.error(f"Error in /predict-demand: {str(e)}")
        return {"error": "Internal Server Error"}, 500
