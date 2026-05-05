import json
import os

class Configuration:
    def __init__(self, path = "life-simulator\config.json"):
        with open(path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get(self, section, key):
        return self.data[section][key]
