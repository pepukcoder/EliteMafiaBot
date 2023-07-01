from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import State, Role


class SendInteractiveMessagesStrategy(Strategy):
    def get_text(self, role: Role, chat_id: int):
        return role.get_interactive_message(chat_id)

    def get_markup(self, role: Role, chat_id: int):
        return role.get_interactive_kb(chat_id)
