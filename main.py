#!/usr/bin/python3

import datetime
from telegram.ext import Updater, CommandHandler
import logging
import bot_functions
import telebot

TOKEN = "1730704056:AAGbswrrc5tR8qnw5p_JxE6Z25J-Uo0pBdw"
RANDOM_MESSAGE_TIME = [(7, 12, 00), (10, 28, 00), (13, 36, 00), (14, 7, 00), (17, 17, 00), (16, 42, 00)]
bot = telebot.TeleBot(TOKEN)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

job = updater.job_queue
job.run_daily(bot_functions.good_morning, time=datetime.time(hour=4, minute=00, second=00))
job.run_daily(bot_functions.good_night, time=datetime.time(hour=18, minute=00, second=00))
for hour, minute, second in RANDOM_MESSAGE_TIME:
    job.run_daily(
        bot_functions.send_random_message, time=datetime.time(hour=hour, minute=minute, second=second)
    )


# @bot.message_handler(content_types=['text'])
# def get_reply(message):
#     if "хорошо" in message.text or "Хорошо" in message.text:
#         bot.send_message(message.from_user.id, "Замечательно, очень рад за тебя)")
#     elif "плохо" in message.text or "Плохо" in message.text:
#         bot.send_message(message.from_user.id, "Зай, не грусти, ты со всем справишься, всё будет хорошо♥")
#     else:
#         bot.send_message(message.from_user.id, ")")
#
#
# bot.polling(none_stop=True, interval=0)
updater.start_polling()
updater.idle()
