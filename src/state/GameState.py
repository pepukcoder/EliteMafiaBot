from dataclasses import dataclass

from src.state import UserState, VoteState, InteractionHistoryRecord


@dataclass
class GameState:
    day: int
    chat_id: int
    status: int
    users: list[UserState]
    votes: list[VoteState]
    interaction_history: list[InteractionHistoryRecord]

