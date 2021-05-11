from telegram.ext import CallbackContext
from random import randint

MY_ID = 472565949
ANDREW_ID = 333294297
RITA_ID = 808833615
GOOD_MORNINGS = ["Доброе утро, любимая)\nХорошего тебе дня😘",
                 "Доброе утро♥️",
                 "Привет) Как спалось?)",
                 "Просыпайся, солнышко♥️",
                 "С добрым утром, котёнок♥️ Очень надеюсь, что ты выпсалась"]
GOOD_NIGHTS = ["Спокойной ночи♥", "Доброй ночи)", "Сладких снов, солнце♥",
               "Спокойной ночи, котёнок😘", "Сладких снов!)", "До завтра, любовь моя♥"]
RANDOM_MESSAGES = ["Привет, как дела?", "Привет, как жизнь?", "Привет, что делаешь?)",
               "Хелоу, май дарлинг, хау а ю?)", "Всем хай, как жизнь?)",
               "Добрый день, как ваша жизнь?", "Привет, как дела, как настроение, что делаешь?",
                "Я скучаю", "Люблю тебя", "Котя, я соскучился", "Солнце, ты самая лучшая!)♥",
                "Зая, ты такая красотка!", "Очень соскучился и хочу к тебе"]


def good_morning(context: CallbackContext) -> None:
    message = GOOD_MORNINGS[randint(0, len(GOOD_MORNINGS) - 1)]
    context.bot.send_message(chat_id=MY_ID, text=message)


def good_night(context: CallbackContext) -> None:
    message = GOOD_NIGHTS[randint(0, len(GOOD_NIGHTS) - 1)]
    context.bot.send_message(chat_id=MY_ID, text=message)


def send_random_message(context: CallbackContext) -> None:
    message = RANDOM_MESSAGES[randint(0, len(RANDOM_MESSAGES) - 1)]
    context.bot.send_message(chat_id=MY_ID, text=message)
