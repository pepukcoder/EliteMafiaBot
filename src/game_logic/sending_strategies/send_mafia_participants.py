from src.game_logic.sending_strategies import Strategy
from src.state import Role


class SendMafiaParticipants(Strategy):
    def get_text(self, role: Role):
        pass

    def get_markup(self, role: Role, chat_id: int):
        pass
