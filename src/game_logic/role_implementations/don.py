from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Don(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "🤵🏻Дон"

    def get_type(self) -> int:
        return Roles.WHORE.value

    def explanation(self) -> str:
        return "- по ночам убивает одного человека. Знает всех мафиози. Ваша цель - убивать и скрывать свою роль."

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()