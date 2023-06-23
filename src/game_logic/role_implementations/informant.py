from aiogram import Bot

from src.state import Role
from src.state.enums import Roles

class Informant(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "🦸🏻Подсосыш"

    def get_type(self) -> int:
        return Roles.INFORMANT.value
    
    def explanation(self) -> str:
        return "- ночью проверяет человека в поисках комиссара, если выберает не его, то роль не показывается. Информация идёт дону, но кто дон - вы не знаете. Ваша цель - помочь дону отыскать комиссара и победить."

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()