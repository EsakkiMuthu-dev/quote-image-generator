import os
from time import time
import bot
import schedule

schedule.every(5).hours.do(bot.main)

while True:
    schedule.run_pending()
    os.system("clear")
    if(os.path.isfile("config/rassouniqz_uuid_and_cookie.json")):
        os.remove("config/rassouniqz_uuid_and_cookie.json")