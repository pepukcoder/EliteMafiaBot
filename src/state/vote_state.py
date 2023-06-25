from dataclasses import dataclass

@dataclass
class VoteState:
    vote_subject: int
    vote_object: int

@dataclass
class ChatVoteState:
    vote_for: int
    vote_against: int
