from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.state import State


def get_all_users_voting_kb(chat_id: int) -> InlineKeyboardMarkup:
    state = State()
    try:
        game = state.games[chat_id]

        inline_markup = InlineKeyboardMarkup(row_width=1)

        for user_state in game.users:
            inline_markup.add(InlineKeyboardButton(text=user_state.first_name,
                                                       callback_data=f"voting_{user_state.user_id}_{chat_id}"))
        print(f"voting_{user_state.user_id}_{chat_id}")

        return inline_markup
    except KeyError:
        print(f"Game {chat_id} not found. roles_unifier/Main.py/get_all_users_voting_kb")


def get_all_users_kb(chat_id: int, interaction_type: int,
                     except_of_users: list[int] = None,
                     except_of_roles: list[int] = None) -> InlineKeyboardMarkup:
    """
    :param chat_id: Game chat id
    :param interaction_type: Int value from src/state/enums/interaction_types
    :param except_of_users: Except of user_id[]
    :param except_of_roles: Except of role src/state/enums/roles
    :return: InlineKeyboardMarkup with needed buttons
    """
    state = State()

    if except_of_users is None:
        except_of_users = []

    if except_of_roles is None:
        except_of_roles = []

    try:
        game = state.games[chat_id]

        inline_markup = InlineKeyboardMarkup(row_width=1)

        for user_state in game.users:
            if (user_state.user_id not in except_of_users
                    and int(user_state.role) not in except_of_roles):
                inline_markup.add(InlineKeyboardButton(text=user_state.first_name,
                                                       callback_data=f"{interaction_type}_{user_state.user_id}_{chat_id}"))

        return inline_markup
    except KeyError:
        print(f"Game {chat_id} not found. roles_unifier/Main.py")
