from peewee import SqliteDatabase

from config import bot
import sqlite3

from telebot import types

from db.user import User
from keyboardMarkup.menu import menu_keyboard

text_Start='Кафе Big Mama это вкусная еда, приветливый коллектив,быстрое обслуживание  и уютная атмосфера.'

text_start_html="<b align='left' >Добро пожаловать в Кафе Big Mama в Киеве</b>\n" \
                "<b align='left'>Кухня: Европейская, Американская, Мексиканская</b>\n" \
                f"<i>{text_Start}</i>\n" \
                "\n" \
                "\n" \
                "\n" \
                '<b>Наш номер: 3800654343</b>'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        User.create(id=message.chat.id, fullname=f'{message.chat.username}',position=1)
    except:
        print("ops")
    finally:
        bot.send_photo(message.chat.id,open('big mama/contact.jpg','rb'),text_start_html,reply_markup=menu_keyboard(message))





