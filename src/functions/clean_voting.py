from src.state import State


def clean_voting(chat_id: int) -> None:
    State().games[chat_id].chat_votes = None
    State().games[chat_id].votes = []
    print(State().games[chat_id])
