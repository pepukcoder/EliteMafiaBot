from abc import abstractmethod, ABC

from aiogram import Bot


class Role(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def get_type(self) -> int: # enum enums/roles.py
        pass

    @abstractmethod
    async def send_interactive_messages(self, bot: Bot):
        pass

    @abstractmethod
    async def send_role_name(self, bot: Bot):
        pass
