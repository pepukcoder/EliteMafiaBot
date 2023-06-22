from aiogram import Bot

from src.state import Role


class Don(Role):
    def get_role_name(self):
        raise NotImplementedError()

    def send_interactive_messages(self, bot: Bot):
        raise NotImplementedError()
