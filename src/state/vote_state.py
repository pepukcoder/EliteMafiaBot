from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class VoteState:
    vote_subject: int
    vote_object: int


@dataclass
class ChatVoteState:
    voting: List[Tuple[int, bool]]  # vote subject, for/against
    vote_for: int
    message_id: int
