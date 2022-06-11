from peewee import *

from db.BaseModel import BaseModel


class Position(BaseModel):
    position_name=TextField()

    