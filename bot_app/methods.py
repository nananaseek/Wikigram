import wikipediaapi

from wikipedia import search
from wikipedia import set_lang

from .app import *
from .models import *


async def w_lang(message):
    text = message.text
    return await do_login(message=message, language=text)


async def do_login(message, language='en'):
    user_id = message.from_user.id
    try:
        user_in_db = await Language.get(user_id=user_id)

        if user_in_db:
            await Language.filter(user_id=user_id).update(language=language)
            return user_in_db.language
    except:
        lang_obj = await Language.create(user_id=user_id, language=language)
    finally:
        return language


async def check_lang(message, chat_id=''):
    if chat_id:
        user_id = chat_id
        user_in_db = await Language.get(user_id=user_id)
        return user_in_db.language
    else:
        user_id = message.from_user.id
        user_in_db = await Language.get(user_id=user_id)
        return user_in_db.language


async def msg_del(query):
    msg = query.message.message_id
    await bot.delete_message(query.from_user.id, msg)


async def type_message(message, query_name=''):
    if query_name:
        message = query_name
        message = message.replace(' ', '_')
        return message
    else:
        message = message.text
        message = message.replace(' ', '_')

        return message


async def check_exist_page(message):
    wiki_wiki = wikipediaapi.Wikipedia(await check_lang(message))
    message = await type_message(message)
    page_py = wiki_wiki.page(str(message))
    return page_py.exists()


async def wiki_text(message, query_name='', query_message=''):
    if query_name:
        wiki_wiki = wikipediaapi.Wikipedia(await check_lang(message=message, chat_id=query_message))
        message = await type_message(message=message, query_name=query_name)
        page_py = wiki_wiki.page(str(message))
    else:
        wiki_wiki = wikipediaapi.Wikipedia(await check_lang(message))
        message = await type_message(message)
        page_py = wiki_wiki.page(str(message))

    return f'{page_py.summary}\n \n{page_py.fullurl}'


async def wiki_query(message):
    set_lang(await check_lang(message))
    return search(message.text, results=3)
