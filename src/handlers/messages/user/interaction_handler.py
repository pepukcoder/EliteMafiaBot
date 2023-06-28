from aiogram import Dispatcher, types, Bot

from src.state import State, InteractionHistoryRecord
from src.state.enums import InteractionTypes
from src.functions import get_role_by_user_id
from src.state.enums import InteractionTypes

from src.misc import TgKeys
from src.state.enums import Roles

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

def register_interaction_handler(dp: Dispatcher):
    @dp.callback_query_handler(regexp="^(-?\d+)_(\d+)_(\-?\d+)$")
    async def interaction_handler(call: types.CallbackQuery):
        await call.message.delete()
        state = State()

        user_id = call.from_user.id
        interaction_type, object_id, chat_id = call.data.split("_")
        game = state.games[int(chat_id)]

        day = state.games[int(chat_id)].day
        state.games[int(chat_id)].interaction_history.append(InteractionHistoryRecord(int(interaction_type),
                                                                                      int(object_id),
                                                                                      int(user_id),
                                                                                      day))
        print(state.games)

        await call.message.answer("Вы выбрали цель")
        print(interaction_type)
        print(InteractionTypes.kill)
        if int(interaction_type) == InteractionTypes.kill or int(interaction_type) == InteractionTypes.check:
            print(interaction_type)
            return
        else:
            await bot.send_message(chat_id=int(chat_id),
                                   text=f"{str(get_role_by_user_id(chat_id=int(chat_id), user_id=int(user_id)))} {get_role_by_user_id(chat_id=int(chat_id), user_id=int(user_id)).get_interaction_message()}")

        # await bot.send_message(chat_id=int(chat_id),
        #                        text=f"{str(get_role_by_user_id(chat_id=int(chat_id), user_id=int(user_id)))} "
        #                             f"{get_role_by_user_id(chat_id=int(chat_id), user_id=int(user_id)).get_interaction_message()}")
        #await call.message.delete()

    @dp.callback_query_handler(regexp="skip_(\-?\d+)")
    async def skip_handler(call: types.CallbackQuery):
        state = State()
        skip_text, chat_id = call.data.split("_")
        user_id = call.from_user.id
        day = state.games[int(chat_id)].day
        state.games[int(chat_id)].interaction_history.append(InteractionHistoryRecord(InteractionTypes.nothing,
                                                                                      0,
                                                                                      user_id,
                                                                                      day))
        await call.message.answer("Вы пропустили ход")
        await bot.send_message(chat_id=int(chat_id),
                               text=f"{str(get_role_by_user_id(chat_id=int(chat_id), user_id=user_id))} решил скуколдиться и забил хуй")
        await call.message.delete()
