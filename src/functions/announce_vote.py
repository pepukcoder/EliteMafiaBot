from aiogram import types, Bot

from src.settings.main import get_language
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def announce_vote(chat_id, bot: Bot):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(get_language(chat_id)['goto_bot'], url='https://t.me/elite_mafia_bot')
    keyboard.add(button)
    await bot.send_message(chat_id,
                           text=get_language(chat_id)['vote_start'],
                           parse_mode='Markdown',
                           reply_markup=keyboard)