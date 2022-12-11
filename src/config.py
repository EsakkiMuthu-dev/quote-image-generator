import os


class Config:
    def __init__(self):
        pass

    def get(self, key):
        config = {
            "image_apiurl": "https://source.unsplash.com/random/400x400",
            "programming_qoute_url": "https://programming-quotes-api.herokuapp.com/quotes/random",
            "image_width": "400",
            "image_height": "400",
        }
        return config[key]

    def loadfont_path(self):
        return os.path.join("fonts", "Roboto-Regular.ttf")

    def loadimage_path(self):
        return os.path.join("image.png")
