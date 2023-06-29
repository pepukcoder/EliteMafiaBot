from aiogram import Dispatcher, types, Bot

from src.functions.is_group import IsPrivate
from src.misc import TgKeys
from src.state import State, GameState
from src.state.enums import Roles

def get_name_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.first_name

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
def register_mafia_chat_handlers(dp: Dispatcher):
    @dp.message_handler(IsPrivate())
    async def send_message_to_mafia_chat(message: types.Message):
        user_id = message.from_user.id
        state = State()

        game = dict(filter(lambda v: user_id in [user.user_id for user in v[1].users], state.games.items()))  # = {chat_id: GameState}

        if game == {}:
            # print("Game not found")
            return

        # get first game state where
        game_state = list(game.values())[0]

        mafia_chat_ids = [user.user_id for user in game_state.users if
                          int(user.role) == Roles.MAFIA or int(user.role) == Roles.DON]

        if len(mafia_chat_ids) < 2:
            # print("Only one mafia")
            return

        if user_id not in mafia_chat_ids:
            # print("User in not mafia")
            return

        mafia_chat_ids.remove(user_id)

        for chat in mafia_chat_ids:
            await bot.send_message(chat_id=chat, text=message.text)