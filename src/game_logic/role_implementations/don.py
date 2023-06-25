from aiogram import Bot, types

from src.game_logic.role_implementations.roles_unifier import get_all_users_kb, get_all_users_voting_kb
from src.state import Role
from src.state.enums import Roles, InteractionTypes
from aiogram.types import InlineKeyboardMarkup


class Don(Role):
    def get_interactive_message(self) -> str:
        return "Выбери, кого ты будешь убивать"

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.don_vote_kill, except_of_roles=[Roles.DON])

    def __str__(self) -> str:
        return "🤵🏻Дон"

    def __int__(self) -> int:
        return Roles.DON.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def interaction_message(self) -> str:
        return "выбрал жертву..."
