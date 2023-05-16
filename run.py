from src import Image, Video
from src.config import Config

if __name__ == "__main__":
    img = Image.Image().main()
    print("Image generated...")
    video = Video.Video().generateVideo(duration=8)
    # app = App()
    # app.start_server()