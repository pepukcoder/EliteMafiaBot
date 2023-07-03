from aiogram import Bot, types

from src.settings import get_language
from src.state import Role, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import Roles, InteractionTypes
from src.game_logic.role_implementations.roles_unifier import get_all_users_kb, InteractiveMessageSender, get_all_users_voting_kb



class Informant(Role):
    def get_interactive_message(self, chat_id: int) -> str:
        return get_language(int(chat_id))['choose_check']
    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.podsos, except_of_roles=[Roles.INFORMANT])

    def get_str(self, chat_id: int) -> str:
        return get_language(chat_id)['informant']

    def __int__(self) -> int:
        return Roles.INFORMANT.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self, chat_id: int) -> str:
        return get_language(int(chat_id))['infa_com']
