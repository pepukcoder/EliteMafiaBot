from dataclasses import dataclass


@dataclass
class RegistrationState:
    chat_id: int
    user_ids: list[int]
    usernames: list[str]