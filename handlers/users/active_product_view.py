from telebot import types

from config import bot
from db.product import Product
from filtres.filtres_product import products_factory
from handlers.users.callback_back import html
from keyboardMarkup.menu import menu_keyboard
from keyboardMarkup.product import product_keyboard
from view.view_html import Html
from view.view_product import view_product


@bot.callback_query_handler(func=lambda callback: callback.data=='start_menu')
def Prodct(callback):
    bot.edit_message_caption(chat_id=callback.message.chat.id,
                              caption=html, message_id=callback.message.id, reply_markup=product_keyboard(callback))



@bot.callback_query_handler(func=None, config=products_factory.filter())
def products_callback(call: types.CallbackQuery):
    callback_data: dict = products_factory.parse(callback_data=call.data)
    product_id = int(callback_data['product_id'])
    print(type(product_id))
    product = Product.get(Product.id==product_id)
    print(type(product))
    view_product(call,product)