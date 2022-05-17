from .Bot import Bot
from .config import Config

def main():
    config = Config()
    bot = Bot(config=config)
    bot.main()