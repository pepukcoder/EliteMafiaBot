from aiogram import Bot
from src.state import State
from src.settings.main import get_language

async def show_alive(chat_id, bot: Bot):
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