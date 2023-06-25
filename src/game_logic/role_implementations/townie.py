from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup

from src.state import Role
from src.state.enums import Roles
from src.game_logic.role_implementations.roles_unifier import get_all_users_voting_kb

class Townie(Role):

    def get_interactive_message(self) -> str:
        pass

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        pass

    def __str__(self) -> str:
        return "👨🏼Мирный житель"

    def __int__(self) -> int:
        return Roles.TOWNIE.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def interaction_message(self) -> str:
        pass
