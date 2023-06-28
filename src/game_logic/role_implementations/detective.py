from src.state import Role, State
from src.state.enums import Roles
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import InteractionTypes
from src.game_logic.role_implementations.roles_unifier import InteractiveMessageSender, get_all_users_kb, get_all_users_voting_kb


class Detective(Role):
    def get_interactive_message(self) -> str:
        return "Выбери действие"

    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        inline_markup = InlineKeyboardMarkup(row_width=1)
        inline_markup.add(InlineKeyboardButton(text="🔍 Проверить игрока",
                                               callback_data=f"detectivecheck_{chat_id}"))
        inline_markup.add(InlineKeyboardButton(text="🔫 Убить игрока",
                                               callback_data=f"detectivekill_{chat_id}"))
        inline_markup.add(InlineKeyboardButton(text=f"🚷Скуколдиться",
                                               callback_data=f"detectiveskip_{chat_id}"))
        return inline_markup

    def __str__(self) -> str:
        return "🕵️Коммисарио Припиздуччи"

    def __int__(self) -> int:
        return Roles.DETECTIVE.value

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    def get_interaction_message(self) -> str:
        return "ага хуй"


class DetectiveLogic:
    @staticmethod
    def get_check_kb(chat_id):
        state = State()
        try:
            game = state.games[chat_id]

            except_of_users = []

            for user_state in game.users:
                if user_state.user_id in [record.interaction_object for record in game.interaction_history if
                                          record.interaction_type is InteractionTypes.check]:
                    except_of_users.append(user_state.user_id)
        except KeyError:
            print(f"Game {chat_id} not found")

        return get_all_users_kb(chat_id, InteractionTypes.check, except_of_roles=[Roles.DETECTIVE])

    @staticmethod
    def get_check_message() -> str:
        return "Выбери, кого ты будешь проверять"

    @staticmethod
    def get_kill_kb(chat_id):
        return get_all_users_kb(chat_id, InteractionTypes.kill, except_of_roles=[Roles.DETECTIVE])

    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        return get_all_users_voting_kb(chat_id)

    @staticmethod
    def get_kill_message() -> str:
        return "Выбери, кого ты будешь убивать"
