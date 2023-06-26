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

    def count_votes(self):
        true_count = 0
        false_count = 0

        if self.chat_votes is not None:
            for vote in self.chat_votes.voting:
                if vote[1] is True:
                    true_count += 1
                elif vote[1] is False:
                    false_count += 1

        return true_count, false_count


    def increase_true_count(self, chat_id: int):
        if self.chat_votes is not None:
            self.chat_votes.voting.append((chat_id, True))

    def increase_false_count(self, chat_id: int):
        if self.chat_votes is not None:
            self.chat_votes.voting.append((chat_id, False))

    def remove_opposite_vote(self, user_id: int):
        if self.chat_votes is None or not self.chat_votes.voting:
            return

        opposite_vote = not any(vote[1] for vote in self.chat_votes.voting if vote[0] == user_id)

        # Check if the user has already voted
        if any(vote[0] == user_id for vote in self.chat_votes.voting):
            self.chat_votes.voting = [(vote[0], vote[1]) for vote in self.chat_votes.voting if vote[0] != user_id]
            self.chat_votes.voting.append((user_id, opposite_vote))