import requests
from src.config import Config
from src.Utils import Utils
import moviepy.editor as np

class Video:

    def __init__(self) -> None:
        self.config = Config()
        self.utils = Utils()
        self.image_path = "image.png"

    def generateVideo(self, duration : int):
        image = np.ImageClip(self.config.loadimage_path(), duration=duration)
        
        clip = np.concatenate_videoclips([image], method="compose")
        
        audio = np.AudioFileClip(self.config.loadmusic_path())
        clip.set_audio(audio)
        
        clip.write_videofile("video.mp4", fps=30)

        print("Video generated...")
