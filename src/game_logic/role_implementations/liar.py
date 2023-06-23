from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Liar(Role):
    def get_type(self) -> int:
        return Roles.LIAR.value

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
