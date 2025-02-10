import yaml
from pathlib import Path


class ConfigManager:
    _single_instance = None

    def __new__(cls, *args, **kwargs):
        if cls._single_instance is None:
            cls._single_instance = super().__new__(cls)
        return cls._single_instance

    def __init__(self):
        config_path = 'config.yaml'
        if not Path(config_path).exists():
            raise ValueError(f"Config file not found at {config_path}.")
        with open(config_path, 'r') as config_file:
            self.config = yaml.safe_load(config_file)

    def get(self, key):
        val = self.config.get(key)
        if val is None:
            raise ValueError(f"Required config key '{key}' not found.")
        return val
