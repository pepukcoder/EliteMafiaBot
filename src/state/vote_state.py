from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class VoteState:
    vote_subject: int
    vote_object: int


@dataclass
class ChatVoteState:
    voting: Optional[List[Tuple[int, bool]]] = None  # vote subject, for/against
    vote_for: Optional[int] = None
    message_id: Optional[int] = None
