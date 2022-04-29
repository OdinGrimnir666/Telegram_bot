from config import bot, Admin

from telebot import types




@bot.message_handler(commands=['admin'])
def admin(message):
    for item in Admin:
         if message.from_user.id== int(item):
             bot.send_message(message.chat.id, f'You admin {message.from_user.id}')
             admin1(message)
         else:
            bot.send_message(message.chat.id, f"No admin  {message.from_user.id}")

def admin1(message):
    kb =types.InlineKeyboardMarkup()
    swith =types.InlineKeyboardButton(text='меню админа',callback_data='/start')
    kb.add(swith)
    bot.send_message(message.chat.id,'Выберите меню админа',reply_markup=kb)
