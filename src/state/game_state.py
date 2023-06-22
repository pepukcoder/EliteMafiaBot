from dataclasses import dataclass

from .user_state import UserState
from .vote_state import VoteState
from .interaction_history_record import InteractionHistoryRecord


@dataclass
class GameState:
    day: int
    chat_id: int
    is_started: bool
    is_day: bool
    users: list[UserState]
    votes: list[VoteState]
    interaction_history: list[InteractionHistoryRecord]

