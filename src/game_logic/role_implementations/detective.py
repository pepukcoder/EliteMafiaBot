from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Detective(Role):
    def get_type(self) -> int:
        return Roles.DETECTIVE.value

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()