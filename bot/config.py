import json
import os

class Config():

    def __init__(self) -> None:
        """Config for the class bot"""
        pass

    def getVariable(self, variable: str) -> str:
        """Get a variable from the config file."""
        with open(self.returnConfigPath(), "r") as f:
            config = json.load(f)
            return config.get(variable)

    def returnConfigPath(self) -> str:
        return os.path.join(os.path.dirname(__file__), "config.json")  