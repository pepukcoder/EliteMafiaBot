from aiogram.types import InlineKeyboardMarkup

from src.game_logic.sending_strategies import Strategy
from src.state import Role


class SendRoleNameMessagesStrategy(Strategy):
    def get_text(self, role: Role):
        return f'Ваша роль - {str(role)}\n\n<a href="https://telegra.ph/Elite-Mafia-roles-06-28"><em>помощь с ролями</em></a>'

    def get_markup(self, role: Role, chat_id: int):
        return InlineKeyboardMarkup()
