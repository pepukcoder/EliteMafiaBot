from aiogram import Bot
from src.state import UserState, State

async def delete_reg(game_chat_id: int, bot: Bot):
    state = State()
    registration_state = state.registrations[game_chat_id]
    await bot.delete_message(chat_id=game_chat_id, message_id=registration_state.message_id)
    state.empty_registrations(game_chat_id)
    print(state.registrations)