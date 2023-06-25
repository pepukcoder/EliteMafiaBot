from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import State, Role


class SendVotingMessages(Strategy):
    def get_voting(role: Role, chat_id: int):
        return role.get_voting_kb(chat_id)

    def get_text(self, role: Role):
        pass

    def get_markup(self, role: Role, chat_id: int):
        pass
