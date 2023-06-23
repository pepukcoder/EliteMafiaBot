from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import UserState, State
from src.game_logic.role_implementations.assign_roles import assign
from src.functions import send_to_pm


class SendRoleNameMessagesStrategy(Strategy):
    async def send(self, game_chat_id: int, bot: Bot):
        state = State()
        users = state.get_game_or_none(game_chat_id).users
        for user in users:
            role_name = str(user.role) if user.role else "👨🏼Мирный житель"
            #await message.reply(f"Username: {user.username}, id: {user.user_id}, Role: {role_name}")
            await send_to_pm(user.user_id, f"Твоя роль - {role_name}")
