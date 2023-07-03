from aiogram import Bot, types

from src.settings import get_language
from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import get_all_users_kb, InteractiveMessageSender, get_all_users_voting_kb


class Lawyer(Role):

    def get_interactive_message(self, chat_id: int) -> str:
        return get_language(chat_id)['lawyer_interaction']

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.justify, except_of_roles=[Roles.LAWYER])

    def get_str(self, chat_id: int) -> str:
        return get_language(chat_id)['lawyer']

    def __int__(self) -> int:
        return Roles.LAWYER.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self, chat_id: int) -> str:
        return get_language(chat_id)['bribe']
