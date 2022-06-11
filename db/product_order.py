import datetime

from db.BaseModel import BaseModel
from peewee import *

from db.order import Order
from db.productbay import Productbay
from db.user import User


class Product_Order(BaseModel):
    order = ForeignKeyField(Order, backref='order')
    product_bay = ForeignKeyField(Productbay, backref='product_bay')


