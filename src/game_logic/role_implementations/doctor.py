from aiogram import Bot

from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import InteractiveMessageSender, get_all_users_kb


class Doctor(Role):
    def get_interactive_message(self) -> str:
        return "Выбери, кого ты будешь лечить"

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
