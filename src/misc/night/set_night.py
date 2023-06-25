from aiogram import Dispatcher, Bot
import os


async def set_night(chat_id, bot):
    night_caption = '*Наступает ночь*'
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'night.mp4')
    with open(path, 'rb') as video_file:
        await bot.send_animation(chat_id=chat_id, animation=video_file, caption=night_caption, parse_mode='Markdown')