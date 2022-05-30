from aiogram import types

from .mesage import *
from .methods import *
from .states import *


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.message):
    await bot.send_message(message.from_user.id, HELLO_MESAGE)
    await do_login(message)


@dp.message_handler(commands=['lang'])
async def language(message: types.message):
    await bot.send_message(message.from_user.id, LANGUAGE_CHOSE)
    await SelectLang.fin.set()
