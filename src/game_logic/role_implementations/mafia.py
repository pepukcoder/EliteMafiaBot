from aiogram import Bot, types

from src.settings import get_language
from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import InteractiveMessageSender, get_all_users_kb, get_all_users_voting_kb


class Mafia(Role):

    def get_interactive_message(self, chat_id: int) -> str:
        return get_language(chat_id)['vote_kill']

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.mafia_vote_kill, except_of_roles=[Roles.DON, Roles.MAFIA])

    def get_str(self, chat_id: int) -> str:
        return get_language(chat_id)['mafia']

    def __int__(self) -> int:
        return Roles.MAFIA.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self, chat_id: int) -> str:
        return get_language(chat_id)['mafia_move']

