from aiogram import Dispatcher, Bot
from src.state import State

async def show_alive(chat_id, bot):
    state = State()

    try:
        users = state.games[chat_id].users

        message = "Живые Игроки:\n"

        for idx, x in enumerate(users):
            message = message + str(idx + 1) + '. ' + str(x.first_name) + "\n"

        print(message)

        await bot.send_message(chat_id, message, parse_mode='Markdown')
    except KeyError:
        print('Errrrrrrrrrrrrrrror')