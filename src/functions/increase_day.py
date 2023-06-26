from src.state import State


async def increment_day(chat_id, day_count):
    state = State()
    game = state.games[chat_id]

    game.day = day_count+1