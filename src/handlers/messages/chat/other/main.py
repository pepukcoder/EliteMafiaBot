from aiogram import Bot, Dispatcher, types
from src.misc import TgKeys
from aiogram.dispatcher.filters import Text, Regexp
import random

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_other_handlers(dp: Dispatcher):

    @dp.message_handler()
    async def tag(message: types.Message):
        words = message.text.split()
        print(words)
        if len(words) == 1 and words[0].lower() == 'тег':
            await message.reply(random.choice(["#непиздит", "#пиздит"]))
        if 'дон' in words:
            await message.reply('гандон')