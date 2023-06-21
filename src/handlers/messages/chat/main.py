from aiogram import Dispatcher

from src.handlers.messages.chat.start import register_start_handlers


def register_chat_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_start_handlers,
    )
    for handler in handlers:
        handler(dp)