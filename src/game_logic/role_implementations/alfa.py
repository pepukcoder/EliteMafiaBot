from aiogram import Bot

from src.state import Role


class Alfa(Role):
    def get_role_name(self):
        raise NotImplementedError()

    async def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
