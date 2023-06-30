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


bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML',proxy="http://proxy.server:3128")


def register_mafia_chat_handlers(dp: Dispatcher):
    @dp.message_handler(IsPrivate())
    async def send_message_to_mafia_chat(message: types.Message):
        user_id = message.from_user.id
        state = State()

        game = dict(filter(lambda v: user_id in [user.user_id for user in v[1].users],
                           state.games.items()))  # = {chat_id: GameState}

        game_death = dict(filter(lambda v: user_id in [user.user_id for user in v[1].initial_roles],
                           state.games.items()))

        if game_death == {}:
            print("Game not found")
            return

        print(game_death)
        # get first game state where
        try:
            game_state = list(game_death.values())[0]
        except:
            game_state = []

        mafia_chat_ids = [user.user_id for user in game_state.users if
                          int(user.role) == Roles.MAFIA or int(user.role) == Roles.DON]

        try:
            l = game_state.death_message[user_id]
            if l[2]:
                await bot.send_message(chat_id=user_id, text="Блять УЖЕ ОТПРАВЛЕНО! сука нахуя ты пишешь")
            else:
                print(user_id, l)
                reply_message_id = l[1] + 1
                await bot.forward_message(chat_id=l[0], from_chat_id=user_id, message_id=reply_message_id)
                l[2] = True
        except:
            if game == {}:
                print("Game not found")
                return

            if len(mafia_chat_ids) < 2:
                # print("Only one mafia")
                return

            if user_id not in mafia_chat_ids:
                # print("User in not mafia")
                return

            mafia_chat_ids.remove(user_id)

            for chat in mafia_chat_ids:
                await bot.send_message(chat_id=chat, text=message.text)
