import requests
from src.config import Config
from PIL import Image as PILImage, ImageDraw, ImageFont, ImageEnhance
from io import BytesIO
from src.Utils import Utils


class Image:
    def __init__(self) -> None:
        self.config = Config()
        self.utils = Utils()
        self.image_path = "image.png"

    def getRandomImage(self):
        url = self.config.get("image_apiurl")
        response = requests.get(url)

        if response.status_code == 200:
            img = PILImage.open(BytesIO(response.content))
            img.save(self.image_path)
            return True
        else:
            return False

    def editImage(self, quote: str, author: str):
        W, H = int(self.config.get("image_width")), int(self.config.get("image_height"))

        image = PILImage.open(self.image_path)

        bri_enhancer = ImageEnhance.Brightness(image=image)

        image = bri_enhancer.enhance(0.3)

        [formatted_quote, length_of_quote] = self.utils.formatTheString(
            quote=quote, author=author
        )
        image_draw = ImageDraw.Draw(image)

        fontsize = 55

        if length_of_quote <= 13:
            fontsize = 65

        image_font = ImageFont.truetype(self.config.loadfont_path(), fontsize)

        _, _, w, h = image_draw.textbbox((0, 0), formatted_quote, font=image_font)
        image_draw.text(
            ((W - w) / 3, (H - h) / 2),
            formatted_quote,
            font=image_font,
            fill=(255, 255, 255, 128),
        )

        image.save(self.image_path)

    def getRandomQuote(self):

        url = self.config.get("quotable_apiurl")
        response = requests.get(url)

        if response.status_code == 200:
            return {"quote": response.json()["content"], "author": response.json()["author"]}
        else:
            return {"quote": "", "author": ""}
        
    def main(self):
        self.getRandomImage()
        quote, author = self.getRandomQuote()["quote"], self.getRandomQuote()["author"]
        self.editImage(author=author, quote=quote)
