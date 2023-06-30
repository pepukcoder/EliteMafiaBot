from aiogram import Dispatcher, types, Bot
from src.functions import delete_reg

from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML',proxy="http://proxy.server:3128")

def register_stop_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['stop_game'])
    async def start_game(message: types.Message):
        chat_id = message.chat.id

        try:
            await delete_reg(chat_id, bot)
            await message.reply("*Игра отменена*", parse_mode='Markdown')
        except:
            await message.reply("*Игры не существует*", parse_mode='Markdown')
