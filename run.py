# from src import App
from src import Image, Video
from src.config import Config

if __name__ == "__main__":
    img = Image.Image().main()
    print("Image generated...")
    video = Video.Video().generateVideo(duration=10)
    # app = App()
    # app.start_server()