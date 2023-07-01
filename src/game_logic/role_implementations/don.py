from aiogram import Bot, types

from src.functions import get_user_id_by_role
from src.game_logic.role_implementations.roles_unifier import get_all_users_kb, get_all_users_voting_kb
from src.misc import TgKeys
from src.settings import get_language
from src.state import Role, State
from src.state.enums import Roles, InteractionTypes
from aiogram.types import InlineKeyboardMarkup
bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

def get_name_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.first_name

class Don(Role):
    def get_interactive_message(self, chat_id: int) -> str:
        return get_language(chat_id)['choose_kill']

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_kb(chat_id, InteractionTypes.don_vote_kill, except_of_roles=[Roles.DON])

    def __str__(self) -> str:
        return "🤵🏻Дон"

    def __int__(self) -> int:
        return Roles.DON.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self, chat_id: int) -> str:
        return get_language(chat_id)['golovorezu']
