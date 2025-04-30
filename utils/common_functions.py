import os 
from src.custom_exception import CustomException
from src.logger import get_logger
import yaml
import pandas as pd

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not in the given path")
        
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Successfully read the yaml file")
            return config  # ✅ Add this line

    except Exception as e:
        logger.error("Error while reading YAML file")
        raise CustomException("Failed to read YAML file", e)  # also fix this comma  