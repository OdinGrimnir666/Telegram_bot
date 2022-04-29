from config import bot, Admin

from telebot import types




@bot.message_handler(chat_id=Admin, commands=['admin'])
def admin_rep(message):
    kb=types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton(text='Расылка',callback_data='newsletter'),
        types.InlineKeyboardButton(text='Админ Меню2',callback_data='admin_menu'),
        types.InlineKeyboardButton(text='Админ Меню3',callback_data='admin_menu'),
        types.InlineKeyboardButton(text='Админ Меню4',callback_data='admin_menu'),
        types.InlineKeyboardButton(text='Админ Меню5',callback_data='admin_menu'),
        types.InlineKeyboardButton(text='Админ Меню6',callback_data='admin_menu')
    )
    bot.send_message(message.chat.id, "You admin",reply_markup=kb)

@bot.message_handler(commands=['admin'])
def admin_rep(message):
          bot.send_message(message.chat.id, 'not you admin')
















