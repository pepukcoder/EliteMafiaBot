from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    async def send(self, game_chat_id: int):
        pass
