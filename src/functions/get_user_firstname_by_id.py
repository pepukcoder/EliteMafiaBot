from src.state import UserState
from src.state import State


def get_user_firstname_by_id(chat_id: int, user_id: int) -> str:
    state = State()
    game = state.games[chat_id]

    return str(list(filter(lambda x: x.user_id is user_id, game.users))[0])
