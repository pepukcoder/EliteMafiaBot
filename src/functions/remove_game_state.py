from src.state import State


def remove_game_state(chat_id: int) -> None:
    del State().games[chat_id]
