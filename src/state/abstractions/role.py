from abc import abstractmethod, ABC

from aiogram import Bot


class Role(ABC):
    @abstractmethod
    def get_role_name(self):
        pass

    @abstractmethod
    async def send_interactive_messages(self, bot: Bot):
        pass
