from aiogram import Bot

from src.settings import get_language
from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import InteractiveMessageSender, get_all_users_kb, get_all_users_voting_kb


class Alfa(Role):
    def get_interactive_message(self, chat_id: int) -> str:
        return get_language(chat_id)['interactive_alfa']

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.fuck_alfa, except_of_roles=[Roles.ALFA])

    def get_str(self, chat_id: int) -> str:
        return get_language(chat_id)['alfa']

    def __int__(self) -> int:
        return Roles.ALFA.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self, chat_id: int) -> str:
        return get_language(chat_id)['interaction_alfa']
