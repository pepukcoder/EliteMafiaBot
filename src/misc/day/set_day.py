from aiogram import Dispatcher, Bot
import os
from src.state import State
from src.state import GameState


async def set_day(chat_id, bot, day_count):
    night_caption = f'*День {day_count}*'
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day.mp4')

    state = State()
    game = state.games[chat_id]

    game.is_day=True
    with open(path, 'rb') as video_file:
        await bot.send_animation(chat_id=chat_id, animation=video_file, caption=night_caption, parse_mode='Markdown')