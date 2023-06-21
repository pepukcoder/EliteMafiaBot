from .game_state import GameState
from .registration_state import RegistrationState


class State:
    __instance = None
    games: list[GameState]
    registrations: list[RegistrationState]

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        State.__instance = None

    def __int__(self):
        self.games = []
        self.registrations = []


    def add_game(self, game: GameState):
        self.games.append(game)

    def remove_game(self, chat_id):
        self.games = [item for item in self.games if item.chat_id != chat_id]
