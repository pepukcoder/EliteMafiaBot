from aiogram import Bot

from src.state import State


def send_interactive_messages(chat_id: int, bot: Bot):
    state = State()
    game = list(filter(lambda x: x.chat_id == chat_id, state.games))[0]
    for user in game.users:
        user.role.send_interactive_messages(bot)
