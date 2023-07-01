from aiogram import Bot

from src.settings import get_language
from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import InteractiveMessageSender, get_all_users_kb, get_all_users_voting_kb


class Doctor(Role):
    def get_interactive_message(self, chat_id: int) -> str:
        return get_language(chat_id)['heal_doc']

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        state = State()
        try:
            game_interaction_history = state.games[chat_id].interaction_history

            except_of = []

            for record in game_interaction_history:
                if (record.interaction_type == InteractionTypes.heal and
                        record.interaction_object == record.interaction_subject):
                    except_of.append(record.interaction_subject)

            return get_all_users_kb(chat_id, InteractionTypes.heal, except_of_users=except_of)

        except KeyError:
            print(f"Game {chat_id} not found. doctor.py")

    def __str__(self) -> str:
        return "👨🏼‍⚕️Доктор"

    def __int__(self) -> int:
        return Roles.DOCTOR.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self, chat_id: int) -> str:
        return f"{get_language(chat_id)['interaction_doc']}..."
