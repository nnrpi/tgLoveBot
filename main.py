#!/usr/bin/python3

import datetime
from telegram.ext import Updater
import logging
import bot_functions

TOKEN = "1730704056:AAGbswrrc5tR8qnw5p_JxE6Z25J-Uo0pBdw"
MY_ID = 472565949

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
job = updater.job_queue
job.run_daily(bot_functions.good_morning, time=datetime.time(hour=4, minute=00, second=00))
job.run_daily(bot_functions.good_night, time=datetime.time(hour=18, minute=00, second=00))
job.run_daily(bot_functions.send_random_message, time=datetime.time(hour=7, minute=12, second=00))
job.run_daily(bot_functions.send_random_message, time=datetime.time(hour=10, minute=23, second=00))
job.run_daily(bot_functions.send_random_message, time=datetime.time(hour=14, minute=49, second=00))

updater.start_polling()
updater.idle()
