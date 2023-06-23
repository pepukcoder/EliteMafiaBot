from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Whore(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "💃🏼Шлюха"

    def get_type(self) -> int:
        return Roles.WHORE.value

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
