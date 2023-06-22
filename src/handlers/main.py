from aiogram import Dispatcher

from src.handlers.messages import register_message_handlers
from src.handlers.game import register_game_handlers

def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_message_handlers,
        register_game_handlers
    )
    for handler in handlers:
        handler(dp)