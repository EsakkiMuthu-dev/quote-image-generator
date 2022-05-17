from PIL import Image

class Utils:
    def findImageIsDarkOrBright(self, image: Image) -> bool:
        """Find if the image is dark or bright."""
        return image.getextrema()[0][0] < 0

    def formatTheString(self, quote: str) -> str:
        """Format the string."""
        word_per_line = 4
        fresh_sentence = ''
        for i, len in enumerate(quote.split()):
            if(i % word_per_line == 0):
                fresh_sentence += '\n'

            fresh_sentence += len + ' '

        return fresh_sentence