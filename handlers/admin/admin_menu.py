from config import bot, Admin

from telebot import types




@bot.message_handler(chat_id=Admin, commands=['admin'])
def admin_rep(message):
    kb=types.InlineKeyboardMarkup()
    swith=types.InlineKeyboardButton(text='Админ Меню',callback_data='admin_menu')
    kb.add(swith)
    bot.send_message(message.chat.id, "You admin",reply_markup=kb)

@bot.message_handler(commands=['admin'])
def not_admin(message):
    bot.send_message(message.chat.id, "not admin")


