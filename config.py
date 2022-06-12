import telebot

from db.user import User

Token=''


from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True


bot=telebot.TeleBot(Token,parse_mode="HTML")





def SetAdmin():
    admin = []
    try:
        admins = User.select().where(User.position == 3)

        for item in admins:
            admin.append(item.id)
    except (Exception):
        print(Exception)
    finally:
        return admin


def SerWorker():
    worker = []
    try:
        workers = User.select().where(User.position == 2)
        for item in workers:
            worker.append(item.id)
    except (Exception):
        print(Exception)
    finally:
        return worker

Admin= SetAdmin()
Worker=SerWorker()
