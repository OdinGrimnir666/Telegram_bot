from telebot import types

from config import bot
from db.basket import Backet
from db.order import Order
from db.product_order import Product_Order
from db.qwery import totalpricebacker
from db.user import User
from filtres.filtes_bay_user import order_filter
from filtres.filtres_product import productbay_basked
from keyboardMarkup.menu import menu_keyboard


def vieworder(order,callback):
    html=f'<b>Номер заказа: {order.id}\nДата заказа: {order.DateTim.strftime("%d:%m:%Y")}\n' \
         f'Время:{order.DateTim.strftime("%H:%M")}\n\n</b>'
    qwery=Product_Order.select().where(Product_Order.order==order.id)


    totalprice=0
    for item in qwery:
        html+=f'<b>{item.product_bay.product.name} {item.product_bay.size.name} {item.product_bay.price} UAH</b>\n'
        totalprice+=item.product_bay.price

    html+=\
        "------------------------------------------------------\n"\
          f'<b>Оплачено: {totalprice}</b>'


    kb=types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Заказ готов',callback_data=order_filter.new(order_id=f'{order.id}')))
    user=User.select().where(User.position==2).where(User.annunciation==True)
    link=User.select().where(User.id==callback.message.chat.id)
    for x in user:
        print(x)
        try:
            bot.send_message(chat_id=x.id,text=html+f' @{link[0].fullname}',reply_markup=kb)
        except(Exception):
            return print(Exception)

    return html




@bot.callback_query_handler(func=lambda callback: callback.data=='pay')
def Prodct(callback):
    qwery=Backet.select().where(Backet.user==callback.message.chat.id)



    count=Backet.select().where(Backet.user==callback.message.chat.id).count()

    if 0<count:
        createorder = Order.create(user=callback.message.chat.id)
        for item in qwery:
            print(item.product_bay)
            Product_Order.create(product_bay=item.product_bay, order=createorder.id)
            item.delete_instance()
        bot.edit_message_caption(message_id=callback.message.id, chat_id=callback.message.chat.id,
                                 caption=vieworder(createorder,callback), reply_markup=menu_keyboard(callback.message))
    else:
        bot.answer_callback_query(callback_query_id=callback.id, text='Плотить нельзя,у вас нет товаров'
                                  , show_alert=True)



@bot.callback_query_handler(func=None, config=order_filter.filter())
def products_callback(call: types.CallbackQuery):
    callback_data: dict = order_filter.parse(callback_data=call.data)
    id = int(callback_data['order_id'])
    print(f'ордер{id}')
    qwery=Order.select().where(Order.id==id)

    bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.id)
    html = f'<b>Номер заказа: {qwery[0].id}\n ' \
           f'Статус: готовый </b>'
    bot.send_message(qwery[0].user.id,html)




