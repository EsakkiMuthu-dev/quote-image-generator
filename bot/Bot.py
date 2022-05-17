from email.policy import strict
import imp
from io import BytesIO
from posixpath import split
import quopri
from PIL import Image, ImageDraw, ImageFont
from .config import Config
import requests
from .Utils import Utils

class Bot():

    def __init__(self, config) -> None:
        """Automatically post a random image and a random programming quote to the instagram."""
        self.config = config
        self.utils = Utils()

    def getRandomImage(self) -> Image:
        """Get a random image from the instagram."""
        url = self.config.getVariable('randomImageUrl')

        # Get the image
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
        fontsize = 32 if len(quote.split()) < 35 else 35
        color = (0,0,0) if self.utils.findImageIsDarkOrBright(Image.open(imagepath)) else (255,255,255)

        if(self.utils.findImageIsDarkOrBright(Image.open(imagepath))):
            # make the image little bit more bright
            image = Image.open(imagepath)
            image = image.point(lambda x: min(x + 100, 255))
            image.save(imagepath)
        else:
            # make the image little bit more dark
            image = Image.open(imagepath)
            image = image.point(lambda x: max(x - 100, 0))
            image.save(imagepath)


        # Add the quote to the image
        img = Image.open(imagepath)
        draw = ImageDraw.Draw(img)
        print(self.config.returnFontPath())
        # load the custom font
        font = ImageFont.truetype(self.config.returnFontPath(), size=fontsize)

        draw.text((x1 / 2, y1 / 2), formatted_quote, font=font, fill=color, anchor="mm")
        # write name on the botom of the image
        fontForName = ImageFont.truetype(self.config.retrunFontForName(), size=15)
        draw.text((x1 /2, y1 - 10 ), "Lazy Insta Bot \U0001f600 Coded and Managed By @rassouniqz...follow for more posts", font=fontForName, fill=color, anchor="ms")
        img.save('img.jpg')

    def PostImagetoInsta(self):
        """Post the image to the instagram."""
        # Get the image
        

    def main(self) -> None:
        """Main function for the bot."""
        # open the image

        
        quote = self.getRandomProgrammingQuote()['en']
        author = self.getRandomProgrammingQuote()['author']

        self.createImage(quote=quote, author=author)
        
        