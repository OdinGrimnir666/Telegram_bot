from db.BaseModel import BaseModel

from peewee import *

from db.product import Product
from db.size import Size


class Productbay(BaseModel):
    product=ForeignKeyField(Product,backref='product')
    size = ForeignKeyField(Size, backref='size')
    price=IntegerField()







