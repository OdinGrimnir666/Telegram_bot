from db.BaseModel import BaseModel

from peewee import *

from db.position import Position


class User(BaseModel):
    id =BigIntegerField(default=0,primary_key=True)
    fullname = CharField()
    phone = CharField(null=True)
    position=ForeignKeyField(Position,backref='position')
    annunciation = BooleanField(default=True)



