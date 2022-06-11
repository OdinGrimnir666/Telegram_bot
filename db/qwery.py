from db.basket import Backet
from db.product import Product
from db.user import User


def activproduct():
    x = Product.select().where(Product.active == True)
    return x


def bascetqwery(callback):
    qwery = Backet.select().where(Backet.user == callback.message.chat.id)
    html = '<b>'

    totalprice = 0
    i=0
    for item in qwery:
        i+=1
        html += f'{i} : {item.product_bay.product.name} {item.product_bay.size.name} {item.product_bay.price} UAH\n'
        totalprice += item.product_bay.price

    html += f"------------------------------------------------------\n" \
            f"К оплате: {totalprice}</b>"
    print(html)

    return html

def totalpricebacker(callback):
    totalprice = 0
    qwery = Backet.select().where(Backet.user == callback.message.chat.id)
    for item in qwery:
        totalprice += item.product_bay.price


    return totalprice*100






