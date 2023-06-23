from src.game_logic.sending_strategies import Strategy


class SendingContext:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    async def send(self, game_chat_id):
        await self._strategy.send(game_chat_id)
