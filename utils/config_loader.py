import yaml

def load_config(file_path):
    """
    Loads configuration from a YAML file.
    """
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise RuntimeError(f"Failed to load config: {str(e)}")
