from dataclasses import dataclass


@dataclass
class RegistrationState:
    chat_id: int
    user_ids: set[int]
    usernames: set[str]