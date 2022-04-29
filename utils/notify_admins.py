from config import Admin


def on_startup_notify(bot):
    for admin in Admin:
        try:
            bot.send_message(admin, "Бот Запущен")
        except Exception as err:
            print(err)
