from peewee import TextField

from db.BaseModel import BaseModel


class Size(BaseModel):
    name=TextField()
