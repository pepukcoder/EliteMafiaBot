from aiogram import Dispatcher, types

from src.state import State, InteractionHistoryRecord


def register_interaction_handler(dp: Dispatcher):

    @dp.callback_query_handler(regexp="^(-?\d+)_(\d+)_(\-?\d+)$")
    async def interaction_handler(call: types.CallbackQuery):
        state = State()
        print('aa')

        user_id = call.from_user.id
        interaction_type, object_id, chat_id = call.data.split("_")

        day = state.games[int(chat_id)].day
        state.games[int(chat_id)].interaction_history.append(InteractionHistoryRecord(interaction_type,
                                                                                     int(object_id),
                                                                                     int(user_id),
                                                                                     int(day)))
        print(state.games)

        await call.message.answer("Вы выбрали цель")
        await call.message.delete()



