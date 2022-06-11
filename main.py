from telebot import custom_filters

from config import bot

import handlers
from db.startdb import StarDb
from filtres.filtres_product import ProductsCallbackFilter
from middlewares.antiflood_middleware import antispam_func

from utils.notify_admins import on_startup_notify
from utils.ser_bot_comands import set_default_commands




bot.register_middleware_handler(antispam_func, update_types=['message'])


bot.add_custom_filter(custom_filters.ChatFilter())

set_default_commands(bot)
on_startup_notify(bot)


bot.add_custom_filter(ProductsCallbackFilter())

bot.add_custom_filter(custom_filters.ChatFilter())







bot.infinity_polling()


