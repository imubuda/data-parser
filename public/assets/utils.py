# utils.py

import os
import json
import logging
from datetime import datetime

def load_config(file_path):
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
            return config
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing JSON in file {file_path}: {e}")
        raise

def save_config(file_path, config):
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)