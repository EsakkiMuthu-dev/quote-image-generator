from src import Image
from src.app import Web

class App:

    def __init__(self) -> None:
        self.image = Image.Image()
        self.web = Web()

    def generate(self):
        self.image.main()

    def start_server(self):
        self.web.start()