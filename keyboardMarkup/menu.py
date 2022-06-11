
from telebot import types

from config import Admin, Worker

google_loccation ='https://www.google.com/maps/place/BIG+MAMA/@50.4425226,30.5219247,20.67z/data=!4m5!3m4!1s0x40d4ce558acedab3:0xf8ecc74aab936002!8m2!3d50.4425242!4d30.5219286'
def inline_callback(text,callback):
    return types.InlineKeyboardButton(text=text,callback_data=callback)
def inline_url(text,url):
    return types.InlineKeyboardButton(text=text,url=url)

def menu_keyboard(message=None):
    menu={'Фирменое Меню 🐂':"start_menu",'Информаця о заведение':'info','позвонить в заведение🦒':'callphone',
    'поделится номером':'phone',"faq":"faq"}

    menu=[inline_callback('Фирменое Меню 🐂','start_menu'),inline_url(text='Адрес 📌',url=google_loccation),
          inline_callback('Последний заказ','last_arder')]
    kb = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for x in menu:
        buttons.append(x)
    kb.add(*buttons)
    if message != None:
        if message.chat.id in Admin:
            kb.add(types.InlineKeyboardButton(text='Настройки', callback_data='sitting'))
        if message.chat.id in Worker:
            kb.add(types.InlineKeyboardButton(text='Настройки', callback_data='sittiтg'))

    return kb