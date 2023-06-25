from aiogram import Bot

from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import InteractiveMessageSender, get_all_users_kb


class Alfa(Role):
    def get_interactive_message(self) -> str:
        return "Выберите, кого вы будете ебать этой ночью"

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.fuck, except_of_roles=[Roles.ALFA])

    def __str__(self) -> str:
        return "🧔🏻‍♂️Альфач"

    def __int__(self) -> int:
        return Roles.ALFA.value
