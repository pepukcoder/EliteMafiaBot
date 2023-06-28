from src.state import State
from src.state import InteractionHistoryRecord

class Delete:
    def delete_all_elements_by_id(chat_id: int, user_ids: list[int]):
        state = State()
        users = state.games[chat_id].users

        # Create a copy of the users list to avoid modifying it during iteration
        users_copy = users.copy()

        for user in users_copy:
            if user.user_id in user_ids:
                users.remove(user)

    def clear_interaction_history(self: int, target_day: int):
        state = State()
        game = state.games[self]
        game.interaction_history[:] = [record for record in game.interaction_history if record.day != target_day]
        print(game.interaction_history)