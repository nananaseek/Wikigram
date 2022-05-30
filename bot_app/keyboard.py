from aiogram.utils.callback_data import CallbackData
from aiogram import types


def search_list_keyboard(wiki_query):
    keyboard = types.InlineKeyboardMarkup()
    count = 0
    for query in wiki_query:
        count = count + 1
        keyboard.add(
            types.InlineKeyboardMarkup(text=query, callback_data=f"search:{query}"))
    return keyboard
