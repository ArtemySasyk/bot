from aiogram.types.web_app_info import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://artemysasyk.github.io/')

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(types.KeyboardButton('Каталог', web_app=web_app)).add('Информация')