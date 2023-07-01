from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import os

from src.settings import get_language
from src.state import State
from src.state import GameState


async def set_night(chat_id, bot):
    night_caption = f"{get_language(chat_id)['set_night']}\n{get_language(chat_id)['city_sleep']}"
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'night.mp4')

    state = State()
    game = state.games[chat_id]

    game.is_day = False

    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(f"{get_language(chat_id)['goto_bot']}", url='https://t.me/elite_mafia_bot')
    keyboard.add(button)

    with open(path, 'rb') as video_file:
        await bot.send_animation(chat_id=chat_id,
                                 animation=video_file,
                                 caption=night_caption,
                                 parse_mode='Markdown',
                                 reply_markup=keyboard)