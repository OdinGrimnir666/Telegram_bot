from peewee import *

from db import productbay
from db.BaseModel import BaseModel
from db.user import User


class Backet(BaseModel):
    user=ForeignKeyField(User,backref='product')
    product_bay=ForeignKeyField(productbay.Productbay, backref='product_bay')

