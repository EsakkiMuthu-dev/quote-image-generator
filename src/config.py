import os


class Config:
    def __init__(self):
        pass

    def get(self, key):
        config = {
            "image_apiurl": "https://source.unsplash.com/1080x1080/?nature",
            "quotable_apiurl": "https://api.quotable.io/random",
            "image_width": "1080",
            "image_height": "1080",
            "duration" : 8
        }
        return config[key]

    def loadfont_path(self, type):
        if type == "main":
            return os.path.join("fonts", "Anton-Regular.ttf")
        return os.path.join("fonts", "OpenSans-Variable.ttf")

    def loadimage_path(self):
        return os.path.join(os.getcwd(), "image.png")
    
    def loadmusic_path(self):
        return os.path.join(os.getcwd(), "sudari.mp3")
