from dataclasses import dataclass

@dataclass
class UserInfo:
    first_name: str
    username: str


@dataclass
class RegistrationState:
    message_id: int
    users: dict[int, UserInfo] # {user_id: UserInfo()}
