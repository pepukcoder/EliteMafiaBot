from aiogram import Dispatcher, types, Bot
from src.functions import delete_reg
from src.settings.main import get_language

from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

def register_stop_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['stop_game'])
    async def start_game(message: types.Message):
        chat_id = message.chat.id

        try:
            await delete_reg(chat_id, bot)
            await message.reply(f"{get_language(chat_id)['game_stop']}", parse_mode='Markdown')
        except:
            await message.reply(f"{get_language(chat_id)['game_notfound']}", parse_mode='Markdown')
