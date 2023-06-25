from aiogram import Bot, types

from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import InteractiveMessageSender, get_all_users_kb


class Mafia(Role):

    def get_interactive_message(self) -> str:
        return "Предложите дону, кого убить"

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.don_vote_kill, except_of_roles=[Roles.DON, Roles.MAFIA])

    def __str__(self) -> str:
        return "🤵🏻Мафия"

    def __int__(self) -> int:
        return Roles.MAFIA.value
