from db.BaseModel import db
from db.additive import Additive
from db.basket import Backet
from db.order import Order
from db.position import Position
from db.product import Product
from db.product_order import Product_Order
from db.productbay import Productbay
from db.size import Size
from db.user import User


def startProduct():
    product = [
        Product.create(name='Фахитос', description=
        'Фирменный лаваш, жареное куриное филе, свежие помидоры, огурцы, морковь по-корейски, белый чесночный соус,томатный соус.'
                       , img='big mama/fahitos.jpeg'),
        Product.create(name='Где хонго', description=
        'Фирменный лаваш, жареное куриное филе, свежие помидоры, маринованные огурцы, шампиньоны на гриле,сыр мацарела,белый соус.',
                       img='big mama/de_hongo.jpeg'),
        Product.create(name='Карденас', description=
        'Фирменный лаваш, жареное куриное филе, смесь мексиканских овощей, свежие помидоры, белый соус,сыр мацарела.',
                       img='big mama/kardanes.jpeg'),
        Product.create(name='Гавайский', description=
        'Фирменный лаваш, жареное куриное филе, смесь мексиканских овощей, ананасы, белый чесночный соус,малина,соус смародины',
                       img='big mama/gabaiski.jpeg'),
        Product.create(name='Терияки', description=
        'Фирменный лаваш, жареное куриное филе, свежие помидоры, авокадо, руккола, белый чесночный соус, кунжут, соус.',
                       img='big mama/falafel_stofu.jpeg'),
        Product.create(name='Бурито', description=
        'Фирменный лаваш, телятина фарш, смесь мексиканских овощей, свежие помидоры,маринованые огурцы,белый чесночный соус,соус барбекю,лук.',
                       img='big mama/burito.jpeg', ),
        Product.create(name='Ролло де мама', description=
        'Фирменный лаваш, жареные на гриле сосиски и салями, 2 вида сыра, соус от шефа, свежие помидоры,маринованые огурцы.',
                       img='big mama/rola_demama.jpeg', ),
        Product.create(name='Ролло де пескадо', description=
        'Фирменный лаваш, копченый хек, смесь мексиканских овощей, свежие помидоры, оливки, соус.',
                       img='big mama/Rolli_de_piskado.jpeg'),
        Product.create(name='Кон сальмон', description=
        'Фирменный лаваш, слабосоленая красная рыба, мягкий сыр, авокадо, оливки, помидоры, тартар соус.',
                       img='big mama/kon_salmon.jpeg'),
        Product.create(name='Фалафель классический', description=
        'Фирменный лаваш, фалафель, хумус, свежие помидоры, морковь по-корейски, огурцы, белый соус чесночный (молочный) томатный соус',
                       img='big mama/falafel_classic.jpeg'),
        Product.create(name='Фалафель карибский', description=
        'Фирменный лаваш, фалафель, хумус, смесь мексиканских овощей, ананасы, малина, белый чесночный соус (молочный) ,соус из смородины.',
                       img='big mama/falafel_karibski.jpeg'),
        Product.create(name='Фалафель c тофу', description=
        'Фирменный лаваш, фалафель, соевый тофу, хумус, свежие помидоры, морковь по-корейски, огурцы,белый соус чесночны(молочный),томатный соус.',
                       img='big mama/falafel_stofu.jpeg', ),
        Product.create(name='BBQ рол', description=
        'Фирменный лаваш, фалафель,кебаб с телятины на огне,свежие помидоры ,мариновоные огурцы,белый чесночный соус,соус барбекю,лук.',
                       img='big mama/falafel_stofu.jpeg', ),
        Product.create(name='Сырный рол каутро', description=
        'Фирменный лаваш,горгондзола,чеддер,моцарела,пармезан,груша,рукола,помидоры,сырный соус.',
                       img='big mama/sirni_sous.jpeg', ),

    ]


def startAdditive():
    addttive = [
        Additive.create(name="Сыр", price='10'),
        Additive.create(name="Ананас", price='10'),
        Additive.create(name="Грибы", price='10')
    ]


def startSize():
    Size.create(name='Pita')
    Size.create(name='Standart')
    Size.create(name='Big')
    Size.create(name='Xl')


def productba(product,size,price):
    return  Productbay.create(product=product,size=size,price=price)

def startPridcyt_bay():
     productba(1,1,60,),productba(1,2,60,),productba(1,2,80),productba(1,3,100)
     productba(2,1,60,), productba(2,2,60,),productba(2,2,80),productba(2,3,100)
     productba(3,1,60,), productba(3,2,60,),productba(3,2,80),productba(3,3,100)
     productba(4,1,60,), productba(4,2,60,),productba(4,2,80),productba(4,3,100)
     productba(5,1,60,),productba(5,2,60,),productba(5,2,80),productba(5,3,100)
     productba(6,1,60,), productba(6,2,60,),productba(6,2,80),productba(6,3,100)
     productba(7,1,60,) ,productba(7,2,60,),productba(7,2,80),productba(7,3,100)
     productba(8,1,60,), productba(8,2,60,),productba(8,2,80),productba(8,3,100)
     productba(9,1,60,), productba(9,2,60,),productba(9,2,80),productba(9,3,100)
     productba(10,1,60,), productba(10,2,60,),productba(10,2,80),productba(10,3,100)
     productba(11,1,60,), productba(11,2,60,),productba(11,2,80),productba(11,3,100)
     productba(12,1,60,), productba(12,2,60,),productba(12,2,80),productba(12,3,100)
     productba(13,1,60,), productba(13,2,60,),productba(13,2,80),productba(13,3,100)
     productba(14,1,60,), productba(14,2,60,),productba(14,2,80),productba(14,3,100)

def startPosition():
    Position.create(position_name='user')
    Position.create(position_name='worker')
    Position.create(position_name='admin')


def StarDb():
    db.create_tables([User, Product, Order,Size, Additive, Productbay,Backet,Position,Product_Order])
    startAdditive()
    startProduct()
    startSize()
    startPosition()
    startPridcyt_bay()
