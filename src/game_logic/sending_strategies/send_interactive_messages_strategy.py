from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import State


class SendInteractiveMessagesStrategy(Strategy):

    async def send(self, game_chat_id: int, bot: Bot):
        state = State()
        try:
            game = state.games[game_chat_id]
            print(game.users)
            for user in game.users:
                await user.role.send_interactive_messages(game_chat_id, bot)
        except KeyError:
            print(f"Game {game_chat_id} not found")

    async def delete(self, game_chat_id: int, bot: Bot):
        pass
