from abc import abstractmethod, ABC

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup


class Role(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __int__(self) -> int:  # enum enums/roles.py
        pass

    @abstractmethod
    def get_interactive_message(self) -> str:
        pass

    @abstractmethod
    def get_voting_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        pass

    @abstractmethod
    def get_interaction_message(self) -> str:
        pass

    @abstractmethod
    def get_interactive_kb(self, chat_id: int) -> InlineKeyboardMarkup:
        pass


