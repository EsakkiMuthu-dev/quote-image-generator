from PIL import Image, ImageDraw, ImageFont
from .config import Config
import requests

class Bot():

    def __init__(self) -> None:
        """Automatically post a random image and a random programming quote to the instagram."""
        pass
        
    def getRandomImage(self) -> Image:
        pass

    def getRandomProgrammingQuote(self) -> str:
        _config = Config()

        quoteRes = requests.get(_config.getVariable("randomProgrammingQuoteUrl"))
        return quoteRes.json()

    def makeImage(self, image: Image, quote: str) -> Image:
        """Make a random image with a random quote."""
        pass

    def main(self) -> None:
        """Main function for the bot."""

        self.getRandomProgrammingQuote()

        # Get a random image
        image = self.getRandomImage()


        
        pass