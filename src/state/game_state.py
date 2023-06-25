from dataclasses import dataclass

from .user_state import UserState
from .vote_state import VoteState, ChatVoteState
from .interaction_history_record import InteractionHistoryRecord
from typing import Optional

@dataclass
class GameState:
    day: int
    is_day: bool
    users: list[UserState]
    votes: list[VoteState]
    interaction_history: list[InteractionHistoryRecord]
    chat_votes: Optional[ChatVoteState] = None