#!/usr/bin/python3

import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import bot_functions

TOKEN = "1730704056:AAGbswrrc5tR8qnw5p_JxE6Z25J-Uo0pBdw"
TEST_TOKEN = "1767534586:AAGGYJjvfuEMENwXqwj14pRajerHuu8HpVw"
RANDOM_MESSAGE_TIME = [(10, 28, 00), (14, 7, 00)]

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

job = updater.job_queue
#job.run_once(bot_functions.once, 5)
job.run_daily(bot_functions.good_morning, time=datetime.time(hour=5, minute=0, second=00))
job.run_daily(bot_functions.good_night, time=datetime.time(hour=18, minute=00, second=00))
for hour, minute, second in RANDOM_MESSAGE_TIME:
    job.run_daily(
        bot_functions.send_random_message, time=datetime.time(hour=hour, minute=minute, second=second)
    )

dispatcher.add_handler(CommandHandler("start", bot_functions.start))
dispatcher.add_handler(CommandHandler("bye", bot_functions.bye))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bot_functions.reply))

updater.start_polling()
updater.idle()
