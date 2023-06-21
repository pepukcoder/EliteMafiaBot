from dataclasses import dataclass

from src.state import UserState, VoteState, InteractionHistoryRecord


@dataclass
class GameState:
    day: int
    chat_id: int
    is_started: bool
    is_day: bool
    users: list[UserState]
    votes: list[VoteState]
    interaction_history: list[InteractionHistoryRecord]

