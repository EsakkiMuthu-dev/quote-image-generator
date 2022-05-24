from email.policy import strict
import imp
from io import BytesIO
import os
from posixpath import split
import quopri
from PIL import Image, ImageDraw, ImageFont
from .config import Config
import requests
from .Utils import Utils
import instabot
class Bot():

    def __init__(self, config) -> None:
        """Automatically post a random image and a random programming quote to the instagram."""
        self.config = config
        self.utils = Utils()
        self.bot = instabot.Bot()
        self.bot.login(username=self.config.getEnvVariable("username"), password=self.config.getEnvVariable("password"))

    def getRandomImage(self) -> Image:
        """Get a random image from the instagram."""
        url = self.config.getVariable('randomImageUrl')

        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        img.save('img.jpg')
        return 'img.jpg'

    def getRandomProgrammingQuote(self) -> str:
        quoteRes = requests.get(self.config.getVariable("randomProgrammingQuoteUrl"))
        return quoteRes.json()


    def createImage(self, quote: str, author: str) -> None:
        """Create an image with a quote and an author."""
        formatted_quote = self.utils.formatTheString(quote) + "\n\n- " + author
        imagepath = self.getRandomImage()

        # image width and height
        x1, y1 = (612, 612)
        fontsize = 36 if len(quote.split()) < 35 else 38
        color = (0,0,0) if self.utils.findImageIsDarkOrBright(Image.open(imagepath)) else (255,255,255)

        if(self.utils.findImageIsDarkOrBright(Image.open(imagepath))):
            image = Image.open(imagepath)
            image = image.point(lambda x: min(x + 100, 255))
            image.save(imagepath)
        else:
            image = Image.open(imagepath)
            image = image.point(lambda x: max(x - 100, 0))
            image.save(imagepath)

        img = Image.open(imagepath)
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(self.config.returnFontPath(), size=fontsize)

        draw.text((x1 / 2, y1 / 2), formatted_quote, font=font, fill=color, anchor="mm")

        fontForName = ImageFont.truetype(self.config.retrunFontForName(), size=15)
        draw.text((x1 /2, y1 - 10 ), "Lazy Insta Bot \U0001f600 Coded and Managed By @rassouniqz...follow for more posts", font=fontForName, fill=color, anchor="ms")
        img.save("bot/img.jpg")
        img.save('img.jpg')

    def PostImagetoInsta(self, quote: str, author: str) -> None:
        """Post the image to the instagram."""

        try:
            imagepath = os.path.join(os.path.dirname(__file__), "img.jpg")
            print("Image Posted")
            caption = f"{self.utils.formatTheString(quote)}\n\n- {author} + \n #lazyinstabot \n Lazy Insta Bot \U0001f600 Coded and Managed By @rassouniqz...follow for more posts \n #programming #coding #python #bot #programmingquotes #daily #codemore codedaily #developer"
           
            self.bot.upload_photo(imagepath, caption=caption)
            print("Posted to instagram")
        except Exception as e:
            print("Failed to post to instagram")

    def main(self) -> None:
        """Main function for the bot."""
        
        quote = self.getRandomProgrammingQuote()['en']
        author = self.getRandomProgrammingQuote()['author']

        print("I am called")

        self.createImage(quote=quote, author=author)
        self.PostImagetoInsta(quote=quote, author=author)
        
        