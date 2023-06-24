from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Townie(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "👨🏼Мирный житель"

    def get_type(self) -> int:
        return Roles.TOWNIE.value

    async def send_interactive_messages(self, user_id:int, bot: Bot):
        await bot.send_message(chat_id=user_id, text="👨🏼Мирный")