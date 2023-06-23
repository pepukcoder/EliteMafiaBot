import random
import enum
from abc import abstractmethod, ABC
#from src.state import UserState
class Role(ABC):
    @abstractmethod
    def get_role_name(self):
        pass

class Don(Role):
    def get_role_name(self):
        raise NotImplementedError()


from dataclasses import dataclass
@dataclass
class UserState:
    username: str
    user_id: int
    role: Role

class Roles(enum.Enum):
    DON = 1
    MAFIA = 2
    LIAR = 3
    INFORMANT = 4
    DOCTOR = 5
    DETECTIVE = 6
    WHORE = 7
    OMEGA = 8
    LAWYER = 9
    ALFA = 10

BAD_ROLES = [Roles.DON, Roles.MAFIA, Roles.LIAR, Roles.INFORMANT]
ADDITIONAL_ROLES = [Roles.WHORE, Roles.OMEGA, Roles.LAWYER, Roles.ALFA]
GOOD_ROLES = [Roles.DETECTIVE, Roles.DOCTOR]

def insert_none_position(lst, value):
    none_indices = [i for i, elem in enumerate(lst) if elem is None]
    if none_indices:
        random_index = random.choice(none_indices)
        lst[random_index] = value

def assign_roles(player_count):
    if player_count == 4:
        return assign_roles_scenario_4()
    elif player_count == 5:
        return assign_roles_scenario_5()
    elif player_count == 6:
        return assign_roles_scenario_6()
    else:
        raise ValueError("Invalid number of players.")

def assign_roles_scenario_4():
    player_roles = [None] * 4
    unique_indices = random.sample(range(4), 2)
    player_roles[unique_indices[0]] = Roles.DON
    player_roles[unique_indices[1]] = Roles.DOCTOR
    return player_roles

def assign_roles_scenario_5():
    player_roles = [None] * 5
    unique_indices = random.sample(range(5), 3)
    player_roles[unique_indices[0]] = Roles.DON
    player_roles[unique_indices[1]] = Roles.DOCTOR
    x = random.sample(ADDITIONAL_ROLES, 1)
    player_roles[unique_indices[2]] = x[0]
    return player_roles


def assign_roles_scenario_6():
    player_roles = assign_roles_scenario_4()

    bad_role = random.choice([role for role in BAD_ROLES if role != Roles.MAFIA and role != Roles.DON])
    player_roles.append(bad_role)
    player_roles.append(Roles.DETECTIVE)
    if random.random() < 0.5:
        insert_none_position(player_roles, random.sample(ADDITIONAL_ROLES, 1)[0])
    else:
        pass
    return player_roles

# Example usage
player_count = 6
player_roles = assign_roles(player_count)

users = [
    UserState(username="Alice", user_id=1, role=player_roles[0]),
    UserState(username="Bob", user_id=2, role=player_roles[1]),
    UserState(username="Charlie", user_id=3, role=player_roles[2]),
    UserState(username="Dave", user_id=4, role=player_roles[3]),
    UserState(username="Pasha", user_id=5, role=player_roles[4]),
    UserState(username="Pasha2", user_id=6, role=player_roles[5])
]

# Print the assigned roles
print(users)