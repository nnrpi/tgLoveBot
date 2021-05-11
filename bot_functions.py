from telegram.ext import CallbackContext

MY_ID = 472565949
ANDREW_ID = 333294297
RITA_ID = 808833615
GOOD_MORNINGS = ["Доброе утро, любимая)\nХорошего тебе дня😘",
                 "Доброе утро♥️",
                 "Привет) Как спалось?)",
                 "Просыпайся, солнышко♥️",
                 "С добрым утром, котёнок♥️ Очень надеюсь, что ты выпсалась"]


def good_morning(context: CallbackContext):
    message = "Hi"
    context.bot.send_message(chat_id=MY_ID, text=message)


def once(context: CallbackContext):
    message = "Luv u)"
    context.bot.send_message(chat_id=MY_ID, text=message)
    context.bot.send_message(chat_id=ANDREW_ID, text=message)


def start(update, context):
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
