from src.state import State


async def increment_day(chat_id):
    state = State()
    game = state.games[chat_id]

    game.day += 1
