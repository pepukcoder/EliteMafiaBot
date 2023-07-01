from aiogram import Bot, Dispatcher, types
from src.misc import TgKeys
from aiogram.dispatcher.filters import Text, Regexp
import random

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_other_handlers(dp: Dispatcher):
    @dp.message_handler(Regexp(r'\bдон\b'))
    async def don(message: types.Message):
        await message.reply("гандон", parse_mode='Markdown')

    @dp.message_handler(Regexp(r'(?i)\bтег\b'))
    async def tag(message: types.Message):
        words = message.text.split()
        if len(words) == 1:
            await message.reply(random.choice(["#непиздит", "#пиздит"]))