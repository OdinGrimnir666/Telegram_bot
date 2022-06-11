import datetime

from peewee import *

from db.BaseModel import BaseModel
from db.user import User


class Order(BaseModel):
    DateTim = DateField(default=datetime.datetime.now)
    DateTime=TimeField(default=datetime.datetime.now)
    active=BooleanField(default=True)
    user = ForeignKeyField(User, backref='user')