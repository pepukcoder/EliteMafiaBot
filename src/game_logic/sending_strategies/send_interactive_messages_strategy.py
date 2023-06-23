from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import State


class SendInteractiveMessagesStrategy(Strategy):

    async def send(self, game_chat_id: int, bot: Bot):
        state = State()
        game = list(filter(lambda x: x.chat_id == game_chat_id, state.games))[0]
        for user in game.users:
            user.role.send_interactive_messages(bot)
