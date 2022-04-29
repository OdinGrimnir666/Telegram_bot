
from config import bot, Admin


@bot.callback_query_handlers(funk=lambda callback: callback.data)
def newsletter(callback):
    if callback.data=='newsletter':

