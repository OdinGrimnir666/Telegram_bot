from telebot import types

from config import bot
from db.basket import Backet
from db.productbay import Productbay
from filtres.filtres_product import productbay_basked
from view.view_product import view_product


@bot.callback_query_handler(func=None, config=productbay_basked.filter())
def products_callback(call: types.CallbackQuery):
    callback_data: dict = productbay_basked.parse(callback_data=call.data)
    id = int(callback_data['productbay_id'])
    qwery = Productbay.select().where(Productbay.id == id)

    count=Backet.select().where(Backet.user==call.message.chat.id).count()
    if 10<=count:
        bot.answer_callback_query(callback_query_id=call.id, text='больше 10 товаров нельзя,перейдите в корзину для оплаты '
                                  , show_alert=True)
    else:
        add = Backet.create(user=call.message.chat.id, product_bay=qwery[0].id)
        print(add.product_bay.product.name)
        bot.answer_callback_query(callback_query_id=call.id, text=f'Вы добавили:{add.product_bay.product.name}'
                                                                  f' Цена:{add.product_bay.price}'
                                  , show_alert=True)

    view_product(product=qwery[0].product,callback=call)





