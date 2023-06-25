from aiogram import Dispatcher, Bot
import os


async def set_day(chat_id, bot, day_count):
    night_caption = f'*День {day_count}*'
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day.mp4')
    with open(path, 'rb') as video_file:
        await bot.send_animation(chat_id=chat_id, animation=video_file, caption=night_caption, parse_mode='Markdown')