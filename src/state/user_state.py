from dataclasses import dataclass

from src.state.abstractions import Role


@dataclass
class UserState:
    username: str
    user_id: int
    role: Role
