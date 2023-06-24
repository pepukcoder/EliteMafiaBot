from dataclasses import dataclass

from src.state.abstractions import Role


@dataclass
class UserState:
    first_name: str
    user_id: int
    role: Role
