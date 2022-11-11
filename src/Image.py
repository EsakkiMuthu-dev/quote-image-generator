import requests
from src.config import config
from PIL import Image as PILImage
from io import BytesIO

class Image:

    def __init__(self) -> None:
        self.config = config.Config()
        pass

    def getRandomImage(self):
        url = self.config.get("image_apiurl")
        response = requests.get(url)

        if response.status_code == 200:
            img = PILImage.open(BytesIO(response.content))
            img.save("image.png")
            return True
        else:
            return False

    def getRandomQuote(self):

        url = self.config.get("programming_qoute_url")
        response = requests.get(url)

        if response.status_code == 200:
            return {
                "quote" : response.json()["en"],
                "author" : response.json()["author"]
            }
        else:
            return False

    
        