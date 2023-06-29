from src.state import State
from aiogram import Bot

class Delete:

    @staticmethod
    async def delete_all_keyboards(chat_id: int, bot: Bot):
        state = State()
        vote_keyboards = state.games[chat_id].voting_keyboards

        for pair in vote_keyboards:
            id, msg_id = pair
            try:
                await bot.delete_message(chat_id=id, message_id=msg_id)
            except:
                print(f"Message does not exist on vote_keyboards id:{id}, message_id:{msg_id}")

    async def delete_all_interaction_keyboards(chat_id: int, bot: Bot):
        state = State()
        interaction_keyboards = state.games[chat_id].interaction_keyboards

        for pair in interaction_keyboards:
            id, msg_id = pair
            try:
                    await bot.delete_message(chat_id=id, message_id=msg_id)
            except:
                print(f"Message does not exist on interaction_keyboards id:{id}, message_id:{msg_id}")


    @staticmethod
    def delete_all_elements_by_id(chat_id: int, user_ids: list[int]):
        state = State()
        users = state.games[chat_id].users

        # Create a copy of the users list to avoid modifying it during iteration
        users_copy = users.copy()

        for user in users_copy:
            if user.user_id in user_ids:
                users.remove(user)

    @staticmethod
    def clear_interaction_history(self: int, target_day: int):
        state = State()
        game = state.games[self]
        game.interaction_history[:] = [record for record in game.interaction_history if record.day != target_day]
        print(game.interaction_history)
