from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import UserState
from src.game_logic.role_implementations.assign_roles import assign
from src.functions import send_to_pm


class SendRoleNameMessagesStrategy(Strategy):
    async def send(self, game_chat_id: int, bot: Bot):
        users=await assign(game_chat_id)
        for user in users:
            role_name = str(user.role) if user.role else "NoneType ЧЁ ЗА ХУЙНЯ это как бля"
            #role_number = user.role.get_type()
            role_number = user.role.explanation()
            #await message.reply(f"Username: {user.username}, id: {user.user_id}, Role: {role_name}")
            await send_to_pm(user.user_id, f"Вы {role_name} {role_number}")
