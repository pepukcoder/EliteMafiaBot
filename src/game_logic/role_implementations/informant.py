from aiogram import Bot, types

from src.state import Role, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import Roles, InteractionTypes
from src.game_logic.role_implementations.roles_unifier import get_all_users_kb, InteractiveMessageSender, get_all_users_voting_kb



class Informant(Role):
    def get_interactive_message(self) -> str:
        return "Выбери, кого ты будешь проверять"
    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.don_vote_kill, except_of_roles=[Roles.INFORMANT])

    def __str__(self) -> str:
        return "🦸🏻Подсосыш"

    def __int__(self) -> int:
        return Roles.INFORMANT.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def interaction_message(self) -> str:
        return "готов подсасываться..."
