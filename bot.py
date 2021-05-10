#!/usr/bin/python3
import datetime
import bot_functions
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1730704056:AAGbswrrc5tR8qnw5p_JxE6Z25J-Uo0pBdw"
MY_ID = 472565949


def callback_alarm(bot, job):
    bot.send_message(chat_id=job.context, text='Wait for another 10 Seconds')

def callback_timer(bot, update, job_queue):
    bot.send_message(chat_id=update.message.chat_id,
                      text='Wait for 10 seconds')
    job_queue.run_repeating(callback_alarm, 10, context=update.message.chat_id)

def Stop_timer(bot, update, job_queue):
    bot.send_message(chat_id=update.message.chat_id,
                      text='Stopped!')
    job_queue.stop()

updater = Updater(TOKEN)
bot = updater.bot
job = updater.job_queue
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', callback_timer, pass_job_queue=True))
dispatcher.add_handler(CommandHandler('stop', Stop_timer, pass_job_queue=True))

updater.start_polling()
updater.idle()
