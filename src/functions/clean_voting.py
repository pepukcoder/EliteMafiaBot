from src.state import State


def clean_voting(chat_id: int) -> None:
    State().games[chat_id].chat_votes = None
    State().games[chat_id].votes = []
    State().games[chat_id].voting_keyboards = []
    State().games[chat_id].users = []
    print(State().games[chat_id])
