from src.game_logic.waiting_strategies import Strategy


class WaitingContext:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    async def wait(self, game_chat_id):
        await self._strategy.wait(game_chat_id)