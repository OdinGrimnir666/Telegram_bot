
from peewee import *

db = SqliteDatabase("big_mama.db")


class BaseModel(Model):
    id=PrimaryKeyField(unique=True)
    class Meta:
        database = db




