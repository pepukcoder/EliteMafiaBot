from src.state import State, GameState


def create_game_state(chat_id: int):
    state = State()

    try:
        game = state.games[chat_id]
    except KeyError:
        state.games[chat_id] = GameState(0, False, users=[], votes=[], interaction_history=[])
    else:
        print(f"game in chat {chat_id} already exists")
