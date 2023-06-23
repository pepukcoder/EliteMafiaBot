from aiogram import Bot

from src.state import Role


class Doctor(Role):
    def get_type(self):
        raise NotImplementedError()

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
