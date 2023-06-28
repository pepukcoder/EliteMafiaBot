from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import os
from src.state import State
from src.state import GameState


async def set_night(chat_id, bot):
    night_caption = '*Наступает ночь*\n' \
                    'В спящем городе скрытые силы разыгрывают свои игры, ' \
                    'а улицы становятся ареной для безжалостных предателей и ' \
                    'теневых авантюристов.'
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'night.mp4')

    state = State()
    game = state.games[chat_id]

    game.is_day = False

    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Перейти в бота', url='https://t.me/elite_mafia_bot')
    keyboard.add(button)

    with open(path, 'rb') as video_file:
        await bot.send_animation(chat_id=chat_id,
                                 animation=video_file,
                                 caption=night_caption,
                                 parse_mode='Markdown',
                                 reply_markup=keyboard)