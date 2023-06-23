from aiogram import Bot

from src.state import Role
from src.state.enums import Roles


class Alfa(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "🧔🏻‍♂️Альфач"

    def get_type(self) -> int:
        return Roles.ALFA.value

    def explanation(self) -> str:
        return "- Альфы нет блять"

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
