from aiogram import types
from aiogram.dispatcher import FSMContext

from .mesage import *
from .methods import *
from .keyboard import *
from .states import *


@dp.message_handler(state=SelectLang.fin)
async def chose_lang(message: types.message, state: FSMContext):
    await bot.send_message(message.from_user.id, LANG_IS.format(await w_lang(message)))

    await state.finish()


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('search'), )
async def user_file_select(query: types.CallbackQuery):
    user_id = query.from_user.id
    query_name = query.data.split(':')[-1]
    text = await wiki_text(message=query.message, query_name=query_name, query_message=query.message.chat.id)
    await bot.send_message(user_id, text)
    await msg_del(query)


@dp.message_handler(commands=['inline'])
async def wiki_search(message):
    user_id = message.from_user.id
    q = await wiki_query(message)
    await bot.send_message(user_id, f'Все що вдалося знаяйти по запиту: {message.text}',
                           reply_markup=search_list_keyboard(q))


@dp.message_handler()
async def message_handler(message: types.message):

    if await check_exist_page(message):
        text = await wiki_text(message)
        await message.reply(text)
    else:
        await wiki_search(message)
