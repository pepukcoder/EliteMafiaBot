from aiogram import Bot, types

from src.settings import get_language
from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import get_all_users_kb, InteractiveMessageSender, get_all_users_voting_kb


class Omega(Role):
    def get_interactive_message(self, chat_id: int) -> str:
        return get_language(chat_id)['omega_minet']

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.switch, except_of_roles=[Roles.OMEGA])

    def __str__(self) -> str:
        return "👦Омежка"

    def __int__(self) -> int:
        return Roles.OMEGA.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self, chat_id: int) -> str:
        return get_language(chat_id)['papik']
