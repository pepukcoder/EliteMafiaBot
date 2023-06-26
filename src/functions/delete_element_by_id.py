from src.state import State
from src.state import InteractionHistoryRecord

class Delete:
    def delete_element_by_id(chat_id: int, user_id: int):
        state = State()
        users = state.games[chat_id].users

        for user in users:
            if user.user_id == user_id:
                users.remove(user)
                break

    def clear_interaction_history(self: int, target_day: int):
        state = State()
        game = state.games[self]
        game.interaction_history[:] = [record for record in game.interaction_history if record.day != target_day]
        print(game.interaction_history)