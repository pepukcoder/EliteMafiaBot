from aiogram import Dispatcher

from src.handlers.messages import register_message_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_message_handlers,
    )
    for handler in handlers:
        handler(dp)