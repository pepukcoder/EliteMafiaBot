from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Informant(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def get_type(self) -> int:
        return Roles.INFORMANT.value

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()