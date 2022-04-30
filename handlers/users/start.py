from peewee import SqliteDatabase

from config import bot
import sqlite3

from telebot import types

@bot.message_handler(commands=['start'])
def send_welcome(message):
    connect = sqlite3.connect("user_id.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
    id INTEGER
    )""")
    connect.commit()
    db = SqliteDatabase('user_id.db')

    cursor.execute(f"SELECT id FROM login_id Where id={message.chat.id}")
    data=cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute('INSERT INTO login_id VALUES(?);', user_id)
        connect.commit()
        bot.send_message(message.chat.id, 'hello')
    else:
        bot.send_message(message.chat.id,"такой пользователь уже есть ")





