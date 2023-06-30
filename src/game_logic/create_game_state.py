from src.state import State, GameState, ChatVoteState


def create_game_state(chat_id: int):
    state = State()

    try:
        game = state.games[chat_id]
    except KeyError:
        state.games[chat_id] = GameState(day=0, is_day=False, users=[], votes=[], interaction_history=[],
                                         chat_votes=ChatVoteState(), initial_roles=[], death_message={})
    else:
        print(f"game in chat {chat_id} already exists")
