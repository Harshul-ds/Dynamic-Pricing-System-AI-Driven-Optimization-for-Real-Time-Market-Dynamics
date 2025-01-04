from flask import Flask
from api.routes import api_blueprint
from utils.logger import get_logger

logger = get_logger("API")
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(api_blueprint, url_prefix="/api")

@app.route("/", methods=["GET"])
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "API is running successfully"}, 200

if __name__ == "__main__":
    try:
        logger.info("Starting API...")
        app.run(host="0.0.0.0", port=5000)
    except Exception as e:
        logger.error(f"Failed to start API: {str(e)}")
