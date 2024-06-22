from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from bot import database as db
from bot import keyboards as kb
import os


#Получения TOKEN бота из файла .env
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


async def on_startup(_):
    print("Запуск бота...")
    await db.db_start()
    print('Бот успешно запущен')


#Обработка кнопки /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if await db.check_user(message.from_user.id):
        await message.answer(text='Привет друг!', reply_markup=kb.keyboard)
    else:
        await message.answer("Ты не наш сотрудник!")


#Обработка кнопки Информация
@dp.message_handler(text='Информация')
async def contacts(message: types.Message):
    if await db.check_user(message.from_user.id):
        await message.answer(
         '\n <b> ИП Берловский Глеб Сергеевич </b> \n'
         '\n <b> ИНН 231216818282 </b>'
         '\n <b> ОГРНИП 322237500445349 </b> \n'
         '\n +7 (918) 194-61-21'
         '\n antaksis@yandex.ru',
          parse_mode="html")
    else:
        await message.answer("Ты не наш сотрудник!")


#Отправка в отдельный чат
@dp.message_handler(content_types=['document', 'photo', 'voice', 'video', 'audio'])
async def check_sticker(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)






#Обработка неизвестных сообщений
@dp.message_handler()
async def answer(message: types.Message):
    await message.answer('Я не понимаю о чем ты!')



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
