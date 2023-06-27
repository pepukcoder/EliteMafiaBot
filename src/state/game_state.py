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

    def decrease_true_count(self, chat_id: int):
        vote = (chat_id, True)
        if self.chat_votes is not None and vote in self.chat_votes.voting:
            self.chat_votes.voting.remove(vote)

    def decrease_false_count(self, chat_id: int):
        vote = (chat_id, False)
        if self.chat_votes is not None and vote in self.chat_votes.voting:
            self.chat_votes.voting.remove(vote)