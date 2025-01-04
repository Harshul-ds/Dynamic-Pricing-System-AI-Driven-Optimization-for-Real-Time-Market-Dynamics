import json
from kafka import KafkaConsumer
from utils.logger import get_logger

logger = get_logger("KafkaConsumer")

def consume_kafka(topic_name, bootstrap_servers, group_id):
    """
    Consumes real-time data from a Kafka topic.
    """
    try:
        consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )
        logger.info(f"Connected to Kafka topic: {topic_name}")
        
        for message in consumer:
            process_message(message.value)
    except Exception as e:
        logger.error(f"Error in Kafka Consumer: {str(e)}")
        raise

def process_message(message):
    """
    Processes a single Kafka message.
    """
    try:
        logger.info(f"Processing message: {message}")
        # Add your custom processing logic here
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise

if __name__ == "__main__":
    consume_kafka(
        topic_name="pricing_data",
        bootstrap_servers="localhost:9092",
        group_id="dynamic_pricing_consumer"
    )
