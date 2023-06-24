from aiogram import Bot, types

from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import InteractiveMessageSender
class Lawyer(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "👨‍⚖️Адвокат"

    def get_type(self) -> int:
        return Roles.LAWYER.value

    async def send_interactive_messages(self, chat_id: int, bot: Bot):
        sender = InteractiveMessageSender()
        await sender.send_interactive_messages(chat_id, bot, self)
