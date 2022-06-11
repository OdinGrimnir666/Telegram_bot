from telebot import types

from config import bot
from db.basket import Backet
from db.qwery import bascetqwery, totalpricebacker

texthtml=''

kb = types.InlineKeyboardMarkup()
kb.add(types.InlineKeyboardButton(text='В меню', callback_data="back_glav_menu"),
       types.InlineKeyboardButton(text='Удалить корзину', callback_data="Delete"))
kb.add(types.InlineKeyboardButton(text='Оплатить', callback_data="pay"))

@bot.callback_query_handler(func=lambda callback: callback.data=='basket')
def Prodct(callback):
    bot.edit_message_media(media=types.InputMediaPhoto(open('big mama/contact.jpg','rb')),message_id=callback.message.id,chat_id=callback.message.chat.id)
    bot.edit_message_caption(message_id=callback.message.id,chat_id=callback.message.chat.id,caption=bascetqwery(callback),
                            reply_markup=kb)

@bot.callback_query_handler(func=lambda callback: callback.data=='Delete')
def Prodct(callback):
    qwery=Backet.select().where(Backet.user==callback.message.chat.id)

    for item in qwery:
        item.delete_instance()
        print('удаление')

    bot.edit_message_caption(message_id=callback.message.id, chat_id=callback.message.chat.id,
                                 caption=bascetqwery(callback), reply_markup=kb)


