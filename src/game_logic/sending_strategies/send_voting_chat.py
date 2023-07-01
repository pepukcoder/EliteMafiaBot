from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import State, Role
from src.functions import send_voting

class SendVotingChat(Strategy):
    def get_voting(role: Role, chat_id: int):
        pass

    def send_voting_chat(chat_id: int, user_id: int, user_firstname: str):
        return send_voting(chat_id=chat_id, user_id=user_id, user_firstname=user_firstname)

    def get_text(self, role: Role, chat_id: int):
        pass

    def get_markup(self, role: Role, chat_id: int):
        pass
