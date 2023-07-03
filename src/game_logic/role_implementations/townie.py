from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup
from src.settings import get_language
from src.state import Role, InteractionHistoryRecord, State
from src.state.enums import Roles
from src.game_logic.role_implementations.roles_unifier import get_all_users_voting_kb

class Townie(Role):

    def get_interactive_message(self, chat_id: int) -> str:
        pass

    def get_interactive_kb(self, chat_id: int) -> None:
        state = State()
        game = state.games[int(chat_id)]
        state.games[int(chat_id)].interaction_history.append(InteractionHistoryRecord(0, 0, 0, game.day))
        return

    def get_str(self, chat_id: int) -> str:
        return get_language(chat_id)['townie']

    def __int__(self) -> int:
        return Roles.TOWNIE.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self, chat_id: int) -> str:
        pass
