from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    async def wait(self, game_chat_id: int):
        pass