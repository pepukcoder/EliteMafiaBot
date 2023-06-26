from aiogram import Dispatcher

from src.handlers.messages.chat.start import register_start_handlers
from src.handlers.messages.chat.stop import register_stop_handlers
from src.handlers.messages.chat.night import register_night_handlers
from src.handlers.messages.chat.vote_handler import register_chat_vote_handler


def register_chat_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_start_handlers,
        register_stop_handlers,
        register_night_handlers,
        register_chat_vote_handler
    )
    for handler in handlers:
        handler(dp)