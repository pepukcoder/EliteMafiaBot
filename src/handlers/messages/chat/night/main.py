from aiogram import Dispatcher, executor, types, Bot
from src.state import State
from src.state import GameState
from src.functions.is_group import IsGroup

from src.misc import TgKeys
from src.state.enums import Roles

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
from src.functions import get_user_id_by_role, get_role_by_user_id


def get_name_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.first_name


def register_night_handlers(dp: Dispatcher):
    state = State()

    @dp.message_handler(IsGroup())
    async def silence(message: types.Message):
        # if night in game state
        try:
            chat_id = message.chat.id
            game = state.games[chat_id]
            user_ids = [user.user_id for user in game.users]
            if game.is_day:
                pass
            else:
                await bot.delete_message(message.chat.id, message.message_id)

            if message.from_user.id not in user_ids:
                await bot.delete_message(message.chat.id, message.message_id)

        except:
            print('User written')
