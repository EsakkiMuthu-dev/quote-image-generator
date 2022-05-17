import json
import os
import dotenv
import random

class Config():

    def __init__(self) -> None:
        """Config for the class bot"""
        pass

    def getVariable(self, variable: str) -> str:
        """Get a variable from the config file."""
        with open(self.returnConfigPath(), "r") as f:
            config = json.load(f)
            return config.get(variable)

    def getEnvVariable(self, variable: str) -> str:
        """Get a variable from the .env file."""
        dotenv.load_dotenv()
        return os.getenv(variable)

    def returnFontPath(self) -> str:
        available_fonts = ['Cinzel-Bold.ttf', 'Cinzel-Regular.ttf', "Koulen-Regular.ttf", "Macondo-Regular.ttf", "OdibeeSans-Regular.ttf"]
        return os.path.join(os.path.dirname(__file__), "assets", "static", random.choice(available_fonts))

    def retrunFontForName(self) -> str:
        return os.path.join(os.path.dirname(__file__), "assets", "static", "Macondo-Regular.ttf")

    def returnAssetsPath(self) -> str:
        return os.path.join(os.path.dirname(__file__), "assets", "static")

    def returnConfigPath(self) -> str:
        return os.path.join(os.path.dirname(__file__), "config.json")  