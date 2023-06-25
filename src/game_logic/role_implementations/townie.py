from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup

from src.state import Role
from src.state.enums import Roles


class Townie(Role):

    def get_interactive_message(self) -> str:
        pass

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        pass

    def __str__(self) -> str:
        return "👨🏼Мирный житель"

    def __int__(self) -> int:
        return Roles.TOWNIE.value
