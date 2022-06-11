from telebot import types

from db.qwery import activproduct
from filtres.filtres_product import products_factory
from keyboardMarkup.backetbatton import basketbatton


def product_keyboard(callback):
    active = activproduct()
    kb = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for i in active:
        button = types.InlineKeyboardButton(text=f'🌯{i.name}', callback_data=products_factory.new(product_id=i.id))
        buttons.append(button)
    kb.add(*buttons)
    kb.add(types.InlineKeyboardButton(text='⬅', callback_data='back_glav_menu'))
    kb.add(basketbatton(callback))
    return kb


