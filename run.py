import os
from time import time
import bot
import schedule

schedule.every(10).minutes.do(bot.main)

while True:
    schedule.run_pending()

# bot.main()