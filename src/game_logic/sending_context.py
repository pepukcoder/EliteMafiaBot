from aiogram import Bot

from src.game_logic.sending_strategies import Strategy
from src.state import State


class SendingContext:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    async def send(self, game_chat_id, bot: Bot):
        state = State()
        try:
            game = state.games[game_chat_id]
            for user in game.users:
                if self._strategy.get_text(user.role):
                    await bot.send_message(user.user_id,
                                       text=self._strategy.get_text(user.role),
                                       reply_markup=self._strategy.get_markup(user.role, game_chat_id))
        except KeyError:
            print(f"Game {game_chat_id} not found")
