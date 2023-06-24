from aiogram import Dispatcher, types, Bot

from src.game_logic.sending_strategies import EmptyArrayAndDeleteRegistrationMessage

from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

def register_stop_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['stop_game'])
    async def start_game(message: types.Message):
        chat_id = message.chat.id

        try:
            await EmptyArrayAndDeleteRegistrationMessage().delete(chat_id, bot)
            await message.reply("*Игра отменена*", parse_mode='Markdown')
        except:
            await message.reply("*Игры не существует*", parse_mode='Markdown')

