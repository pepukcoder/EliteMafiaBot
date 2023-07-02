from aiogram import Bot, Dispatcher, types
from src.misc import TgKeys
from src.settings.main import get_language
import random

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_other_handlers(dp: Dispatcher):

    @dp.message_handler()
    async def tag(message: types.Message):
        chat_id = message.chat.id
        words = message.text.lower().split()
        if len(words) == 1 and words[0].lower() == get_language(chat_id)['h_tag']:
            await message.reply(random.choice([get_language(chat_id)['h_true'], get_language(chat_id)['h_false']]))
        if get_language(chat_id)['h_don'] in words:
            await message.reply(get_language(chat_id)['h_gdon'])