from aiogram import Dispatcher

from src.handlers.messages.chat.start import register_start_handlers
from src.handlers.messages.chat.stop import register_stop_handlers
from src.handlers.messages.chat.night import register_night_handlers

def register_chat_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_start_handlers,
        register_stop_handlers,
        register_night_handlers,
    )
    for handler in handlers:
        handler(dp)