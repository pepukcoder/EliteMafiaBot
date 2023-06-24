from .game_state import GameState
from .registration_state import RegistrationState


class State:
    __instance = None
    games: dict[int, GameState]  # {chat_id: GameState}
    registrations: dict[int, RegistrationState]  # {chat_id: RegistrationState}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.registrations = {}  # {chat_id: RegistrationState}
            cls.__instance.games = {}  # {chat_id: GameState}

        return cls.__instance

    def __del__(self):
        State.__instance = None
