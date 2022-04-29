from telebot import types
from config import bot

def set_default_commands(bot):
    bot.set_my_commands([
        types.BotCommand("start","Запустить бота"),
        types.BotCommand("admin", "Админка"),
    ])