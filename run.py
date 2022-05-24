import os
from time import time
import bot
import schedule

schedule.every(30).minutes.do(bot.main)

while True:
    schedule.run_pending()
    if(os.path.isfile("config/rassouniqz_uuid_and_cookie.json")):
        os.remove("config/rassouniqz_uuid_and_cookie.json")