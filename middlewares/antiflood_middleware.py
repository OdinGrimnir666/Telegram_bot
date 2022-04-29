import time

from telebot import TeleBot
from telebot.types import Message

DATA = {}

def antispam_func(bot: TeleBot, message: Message):
    bot.temp_data = {message.from_user.id : 'OK'}
    if DATA.get(message.from_user.id):
        if int(time.time()) - DATA[message.from_user.id] < 2:
            bot.temp_data = {message.from_user.id : 'FAIL'}
            bot.send_message(message.chat.id, 'Подожди перед отправкой')
    DATA[message.from_user.id] = message.date