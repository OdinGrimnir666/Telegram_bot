from db.basket import Backet
from telebot import types

def basketbatton(callback):
    qwery=Backet.select().where(Backet.user==callback.message.chat.id).count()
    print(qwery)

    return types.InlineKeyboardButton(text=f'Корзина({qwery})',callback_data='basket')