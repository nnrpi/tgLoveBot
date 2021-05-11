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
j = updater.job_queue
j.run_daily(bot_functions.good_morning, time=datetime.time(hour=9, minute=8, second=00))

updater.start_polling()
updater.idle()
