from aiogram import Dispatcher

from src.handlers.messages.user.mafia_chat import register_mafia_chat_handlers
from src.handlers.messages.user.detective_interaction_choice_handler import \
    register_detective_interaction_choice_handler
from src.handlers.messages.user.interaction_handler import register_interaction_handler
from src.handlers.messages.user.start import register_start_handler
from src.state import State, UserInfo
from src.misc import TgKeys
from src.handlers.messages.user.vote_handler import register_vote_handler


def register_user_handlers(dp: Dispatcher):
    handlers = (
        register_start_handler,
        register_interaction_handler,
        register_detective_interaction_choice_handler,
        register_vote_handler,
        register_mafia_chat_handlers
    )

    for handler in handlers:
        handler(dp)
