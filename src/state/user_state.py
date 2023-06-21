from dataclasses import dataclass


@dataclass
class UserState:
    username: str
    user_id: int
    role: int #enum
