from aiogram import Dispatcher, types

from src.state import State, InteractionHistoryRecord


def register_interaction_handler(dp: Dispatcher):

    @dp.callback_query_handler(regexp="\d*_\d*_\d*")
    async def interaction_handler(call: types.CallbackQuery):
        state = State()

        user_id = call.from_user.id
        interaction_type, object_id, chat_id = call.data.split("_")

        try:
            day = state.games[chat_id].day
            state.games[chat_id].interaction_history.append(InteractionHistoryRecord(interaction_type,
                                                                                     object_id,
                                                                                     user_id,
                                                                                     day))
            print(state)

            await call.message.answer("Вы выбрали цель")
            await call.message.delete()
        except KeyError:
            print(f"Game {chat_id} not found")



