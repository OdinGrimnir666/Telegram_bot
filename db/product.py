from db.BaseModel import BaseModel
from peewee import *


class Product(BaseModel):
    name=CharField()
    img=TextField()
    description=TextField()
    active=BooleanField(default=True)