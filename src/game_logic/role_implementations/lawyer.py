from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Lawyer(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "👨‍⚖️Адвокат"

    def get_type(self) -> int:
        return Roles.LAWYER.value

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
