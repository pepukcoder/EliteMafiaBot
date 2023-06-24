from abc import ABC, abstractmethod

from aiogram import Bot


class Strategy(ABC):
    @abstractmethod
    async def send(self, game_chat_id: int, bot: Bot):
        pass

    @abstractmethod
    async def delete(self, game_chat_id: int, bot: Bot):
        pass
