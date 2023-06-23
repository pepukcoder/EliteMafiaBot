from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Alfa(Role):
    def get_type(self) -> int:
        return Roles.ALFA.value

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
