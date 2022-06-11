import time

from telebot import types

from config import bot
from db import user
from db.order import Order
from db.product_order import Product_Order
from db.user import User
from handlers.users.start import text_start_html
from keyboardMarkup.menu import menu_keyboard
from keyboardMarkup.product import product_keyboard

html = "<b>Наше любимое меню</b>"


@bot.callback_query_handler(func=lambda callback: callback.data == 'start_callback')
def Prodct(callback):
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
    bot.send_photo(callback.message.chat.id, open('big mama/contact.jpg', 'rb'), html,
                   reply_markup=product_keyboard(callback))


@bot.callback_query_handler(func=lambda callback: callback.data == 'back_glav_menu')
def Prodct(callback):
    bot.edit_message_caption(message_id=callback.message.id, chat_id=callback.message.chat.id,
                             caption=text_start_html, reply_markup=menu_keyboard(callback.message))


@bot.callback_query_handler(func=lambda callback: callback.data == 'last_arder')
def lastorder(callback):
    qwerye = Order.select().where(Order.user == callback.message.chat.id)
    print(qwerye.count())
    print(qwerye[0].id)
    qwery = Product_Order.select().where(Product_Order.order == qwerye[-1].id)

    print(qwery)
    print(qwery.count())

    import time

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    html = f'<b>Номер заказа: {qwery[0].order.id}\nДата заказа: {qwery[0].order.DateTim.strftime("%d:%m:%Y")}\n' \
           f'Время: {qwery[0].order.DateTime.strftime("%H:%M")}\n\n</b>'

    print(html)
    print(qwery[0].order.DateTim)

    qwery1 = Product_Order.select().where(Product_Order.order == qwery[-1].order.id)

    totalprice = 0
    for item in qwery1:
        html += f'<b>{item.product_bay.product.name} {item.product_bay.size.name} {item.product_bay.price} UAH</b>\n'
        totalprice += item.product_bay.price

    html += \
        "------------------------------------------------------\n" \
        f'<b>Оплачено: {totalprice}</b>'

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(
        text='⬅',
        callback_data='start_callback'
    ))

    bot.edit_message_caption(message_id=callback.message.id, chat_id=callback.message.chat.id,
                             caption=html, reply_markup=kb)
