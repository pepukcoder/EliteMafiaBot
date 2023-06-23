from aiogram import Dispatcher, Bot
from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

async def send_to_pm(chat_id, message):
    await bot.send_message(chat_id, message, parse_mode='Markdown')