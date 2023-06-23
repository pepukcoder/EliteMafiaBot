from src.state import State, GameState


def create_game_state(chat_id: int):
    state = State()

    game = state.get_game_or_none(chat_id)

    if game is not None:
        print(f"game in chat {chat_id} already exists")
        return

    state.games.append(GameState(0, chat_id, False, users=[], votes=[], interaction_history=[]))
