from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import UserState, State
from src.game_logic.role_implementations.assign_roles import assign
from src.functions import send_to_pm

class EmptyArrayAndDeleteRegistrationMessage(Strategy):
    async def delete(self, game_chat_id: int, bot: Bot):
        state = State()
        registration_state = state.registrations[game_chat_id]
        await bot.delete_message(chat_id=game_chat_id, message_id=registration_state.message_id)
        state.empty_registrations(game_chat_id)
        print(state.registrations)
    async def send(self, game_chat_id: int, bot: Bot):
        pass