from aiogram import Dispatcher, Bot

from src.settings import get_language
from src.state import State

async def show_alive(chat_id, bot):
    state = State()

    try:
        users = state.games[chat_id].users

        message = f"{get_language(chat_id)['alive']}:\n"

        for idx, x in enumerate(users):
            message = message + str(idx + 1) + '. ' + str(x.link) + "\n"

        print(message)

        await bot.send_message(chat_id, message, parse_mode='Markdown')
    except KeyError:
        print('Error')