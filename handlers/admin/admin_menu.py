import sqlite3

from config import bot, Admin

from telebot import types




@bot.message_handler(chat_id=Admin, commands=['admin'])
def admin_rep(message):
    kb=types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton(text='Расылка',callback_data='newsletter'),
    )
    bot.send_message(message.chat.id, "You admin",reply_markup=kb)

@bot.message_handler(commands=['admin'])
def admin_rep(message):
          bot.send_message(message.chat.id, 'not you admin')


@bot.callback_query_handler(func=lambda callback: callback.data)
def newsletter(callback):
    if callback.data == 'newsletter':
        sent = bot.reply_to(callback.message,"оставьте отзвв")
        bot.register_next_step_handler(sent, letter)



def letter(message):
    connect = sqlite3.connect("user_id.db")
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM login_id WHERE id ")
    result = cursor.fetchall()
    msg = message.text
    for x in result[0]:
        bot.send_message(x,str(msg))

















