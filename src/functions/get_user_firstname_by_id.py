from src.state import UserState
from src.state import State

class GetFirstName:
    def get_user_firstname_by_id(chat_id: int, user_id: int):
        state = State()
        game = state.games[chat_id]

        for user in game.users:
            if user.user_id == user_id:
                return user.first_name