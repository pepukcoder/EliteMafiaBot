from dataclasses import dataclass


@dataclass
class VoteState:
    vote_subject: int
    vote_object: int
