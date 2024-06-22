import sqlite3 as sq

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.main import bot

db = sq.connect("O'Donuts.db")
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "tg_id TEXT,"
                "place TEXT,"
                "cart_id TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "photo TEXT,"
                "desc TEXT,"
                "brand TEXT)")
    db.commit()


async def check_user(user_id):
    cur.execute("SELECT * FROM users WHERE tg_id = ?", (user_id,))
    result = cur.fetchone()
    return result is not None

async def send_monthly_message():
    cur.execute("SELECT tg_id FROM users")
    users = cur.fetchall()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text='❗️Сегодня 25 число, не забудь провести инвентаризацию!')

scheduler = AsyncIOScheduler()
scheduler.add_job(send_monthly_message, 'cron', day='25', hour='10', minute='10')
scheduler.start()

async def send_weekly_message():
    cur.execute("SELECT tg_id FROM users")
    users = cur.fetchall()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text='❗️Сегодня день оформления заявок на продукцию, проверь наличие товара, если чего то нет, не забудь заказать!')

scheduler = AsyncIOScheduler()
scheduler.add_job(send_weekly_message, 'cron', day_of_week='mon,thu', hour='10', minute='10')
scheduler.start()


# Данные для проверки или добавления
#id_to_check = 529424412
#place_to_check = "Затон 1"

# Проверяем наличие записи с указанным id
#cur.execute("SELECT * FROM users WHERE tg_id = ? AND place = ?", (id_to_check, place_to_check))
#result = cur.fetchone()
#if result:
#    print("Запись с таким ID уже существует.")
# Добавление нового пользователя
#else:
#    cur.execute("INSERT INTO users (tg_id, place) VALUES (?,?)", (id_to_check, place_to_check))
#    db.commit()
#    print("Новая запись успешно добавлена.")




