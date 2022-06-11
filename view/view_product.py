from telebot import types

from config import bot
from db.product import Product
from db.productbay import Productbay
from filtres.filtres_product import productbay_basked
from keyboardMarkup.backetbatton import basketbatton
from view.view_html import ProductHtml


def view_product(callback,product):
    file_name=open(product.img,'rb')
    kb=types.InlineKeyboardMarkup(row_width=2)

    add_del=['Добавить в корзину','Удалить с корзины']


    x=Productbay.select().where(Productbay.product==product.id)
    kb.add(types.InlineKeyboardButton(text=f'{add_del[0]} Pita {x[0].price} UAH',callback_data=productbay_basked.new(productbay_id=f'{x[0].id}')))
    kb.add(types.InlineKeyboardButton(text=f'{add_del[0]} Standart {x[1].price} UAH',callback_data=productbay_basked.new(productbay_id=x[1].id)))
    kb.add(types.InlineKeyboardButton(text=f'{add_del[0]} Big {x[2].price} UAH',callback_data=productbay_basked.new(productbay_id=x[2].id)))
    kb.add(types.InlineKeyboardButton(text=f'{add_del[0]} XL {x[3].price} UAH',callback_data=productbay_basked.new(productbay_id=x[3].id)))


    kb.add(types.InlineKeyboardButton(text='⬅',callback_data='start_callback'))
    kb.add(basketbatton(callback))
    # bot.delete_message(chat_id=callback.message.chat.id,message_id=callback.message.id)
    # bot.send_photo(callback.message.chat.id,file_name,ProductHtml(product),reply_markup=kb)

    bot.edit_message_media(media=types.InputMediaPhoto(file_name),
                           message_id=callback.message.id, chat_id=callback.message.chat.id)
    bot.edit_message_caption(message_id=callback.message.id, chat_id=callback.message.chat.id,
                             caption=ProductHtml(product), reply_markup=kb)



