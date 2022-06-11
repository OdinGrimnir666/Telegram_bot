from peewee import *
from db.BaseModel import BaseModel


class Additive(BaseModel):
    name=CharField()
    price=IntegerField()
    active=BooleanField(default=True)
