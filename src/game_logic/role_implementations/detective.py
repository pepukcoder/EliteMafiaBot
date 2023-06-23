from aiogram import Bot

from src.state import Role


class Detective(Role):
    def get_type(self):
        raise NotImplementedError()

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
