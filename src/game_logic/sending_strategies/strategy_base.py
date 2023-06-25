from abc import ABC, abstractmethod

from aiogram import Bot

from src.state import Role


class Strategy(ABC):
    @abstractmethod
    def get_text(self, role: Role):
        pass

    @abstractmethod
    def get_markup(self, role: Role, chat_id: int):
        pass
