from aiogram import Dispatcher, executor, types, Bot
from src.state import State
from src.state import GameState
from src.functions.is_group import IsGroup

from src.misc import TgKeys
bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_night_handlers(dp: Dispatcher):
    state = State()
    @dp.message_handler(IsGroup())
    async def silence(message: types.Message):
        #if night in game state
        try:
            chat_id = message.chat.id
            game = state.games[chat_id]
            if game.is_day:
                pass
            else:
                await bot.delete_message(message.chat.id, message.message_id)
        except:
            print('user written')