from dataclasses import dataclass


@dataclass
class UserState:
    user_id: int
    role: int #enum
