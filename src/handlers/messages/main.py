from aiogram import Dispatcher

from src.handlers.messages.user import register_user_handlers
from src.handlers.messages.chat import register_chat_handlers

def register_message_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_chat_handlers,
        register_user_handlers,
    )
    for handler in handlers:
        handler(dp)
