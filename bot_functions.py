from telegram import Update
from telegram.ext import CallbackContext
from random import randint

TOKEN = "1730704056:AAGbswrrc5tR8qnw5p_JxE6Z25J-Uo0pBdw"
MY_ID = 472565949
ANDREW_ID = 333294297
RITA_ID = 808833615
PATH = "/home/ubuntu/PycharmProjects/tgLoveBot/users_id.txt"
MYAUMUR = {"Мяу": "Мур", "мяу": "мур", "Мур": "Мяу", "мур": "мяу"}
GOOD_MORNINGS = ["Доброе утро, солнце)\nХорошего тебе дня😘",
                 "Доброе утро♥️",
                 "Привет) Как спалось?)",
                 "Просыпайся, солнышко♥️",
                 "С добрым утром, котёнок♥️ Очень надеюсь, что тебе хорошо спалось"]
GOOD_NIGHTS = ["Спокойной ночи♥", "Доброй ночи)", "Сладких снов, солнце♥",
               "Спокойной ночи, котёнок😘", "Сладких снов!)", "До завтра, любовь моя♥"]
RANDOM_MESSAGES = ["Привет, как дела?", "Привет, как жизнь?", "Привет, что делаешь?)",
                   "Хелоу, май дарлинг, хау а ю?)", "Всем хай, как жизнь?)",
                   "Добрый день, как ваша жизнь?", "Привет, как дела, как настроение, что делаешь?",
                   "Я скучаю", "Люблю тебя", "Котя, я скучаю", 
                   "Солнце, ты самый лучший человек из всех, кого я знаю!)♥", "Очень скучаю и хочу к тебе"]


def good_morning(context: CallbackContext) -> None:
    message = GOOD_MORNINGS[randint(0, len(GOOD_MORNINGS) - 1)]
    for id in open(PATH):
        context.bot.send_message(chat_id=int(id[:-1]), text=message)


def good_night(context: CallbackContext) -> None:
    message = GOOD_NIGHTS[randint(0, len(GOOD_NIGHTS) - 1)]
    for id in open(PATH):
        context.bot.send_message(chat_id=int(id[:-1]), text=message)


def send_random_message(context: CallbackContext) -> None:
    message = RANDOM_MESSAGES[randint(0, len(RANDOM_MESSAGES) - 1)]
    for id in open(PATH):
        context.bot.send_message(chat_id=int(id[:-1]), text=message)


def once(context: CallbackContext) -> None:
    message = """Привет, у меня набралось уже какое-то количество функционала, вероятно, вы не все о нём всё знаете, так что давайте я расскажу:
    1) /start - вы получите приветное сообщение и добавитесь в список тех, кто получает милую рассылку
    2) /bye - вы получите прощальное сообщение и исключитесь из списка получающих милую рассылку
    3) На сообщение со словами \"хорошо\" и \"плохо\" вы получаете определённые ответы
    4) Как и на сообщения со словами \"мур\" и \"мяу\"
    Возможно, фичи будут добавляться, следите за новостями!
    Всем счастья и любви)"""
    for id in open(PATH):
        context.bot.send_message(chat_id=int(id[:-1]), text=message)


def _add_user_by_id(new_id: int) -> None:
    if str(new_id) + "\n" in open(PATH):
        return
    users_id = open(PATH, "a")
    users_id.write(str(new_id) + "\n")
    users_id.close()

def _remove_user_by_id(removing_id: int) -> None:
    if str(removing_id) + "\n" not in open(PATH):
        return
    users_id = [int(user_id) for user_id in open(PATH)]
    new_users_id = open(PATH, "w")
    for user_id in users_id:
        if user_id != removing_id:
            new_users_id.write(str(user_id) + "\n")
    new_users_id.close()


def start(update: Update, _: CallbackContext) -> None:
    _add_user_by_id(update.message.chat_id)
    update.message.reply_text("Hello darling♥")


def bye(update: Update, _: CallbackContext) -> None:
    _remove_user_by_id(update.message.chat_id)
    update.message.reply_text("Bye, it was nice to chat w/ u😊")


def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def reply(update: Update, _: CallbackContext) -> None:
    user_message = update.message.text
    if "хорошо" in user_message or "Хорошо" in user_message:
        update.message.reply_text("Замечательно, очень рад за тебя)")
    elif "плохо" in user_message or "Плохо" in user_message:
        update.message.reply_text("Зай, не грусти, ты со всем справишься, всё будет хорошо♥")
    elif user_message in MYAUMUR:
        update.message.reply_text(MYAUMUR[user_message])
    else:
        update.message.reply_text(")")
