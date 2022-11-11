from src import Image

class App:

    def __init__(self) -> None:
        self.image = Image.Image()

    def generate(self):
        if self.image.getRandomImage():
            print("Image getted successfully!")
        else:
            print("Error generating image!")