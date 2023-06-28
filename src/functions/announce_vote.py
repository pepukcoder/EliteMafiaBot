from aiogram import types, Bot

from src.state import State, ChatVoteState
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def announce_vote(chat_id, bot: Bot):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Перейти в бота', url='https://t.me/elite_mafia_bot')
    keyboard.add(button)
    await bot.send_message(chat_id,
                           text='Голосование началось!',
                           parse_mode='Markdown',
                           reply_markup=keyboard)