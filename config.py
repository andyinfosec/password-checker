import json
from pathlib import Path
from types import SimpleNamespace

# Loads configuration settings from json file

def load_json():
    CONFIG_PATH = Path(__file__).parent/"config.json"
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)

    return config

# Validates  configuration values 

def validate_config(config):   
    rules = config["rules"]

    if rules["min_length"] < 1:
        raise ValueError("Minimum length must be more than 0")

    if rules["max_length"] < rules["min_length"]:
        raise ValueError("Maximum length must be more than minimum length")

config = load_json()
validate_config(config)

# Creates an object from the json data. the key becomes the attribute name.

RULES = SimpleNamespace(**{
    key.upper(): value
    for key, value in config["rules"].items()
})


