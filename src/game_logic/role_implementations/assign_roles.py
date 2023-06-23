import random
import enum
from abc import abstractmethod, ABC
#from src.state import UserState

from src.state.enums import Roles
from src.game_logic.role_implementations import Don, Mafia, Liar, Informant, Doctor, Detective, Whore, Omega, Lawyer, Alfa

BAD_ROLES = [Don(), Mafia(), Liar(), Informant()]
ADDITIONAL_ROLES = [Whore(), Omega(), Lawyer(), Alfa()]
GOOD_ROLES = [Detective(), Doctor()]

def insert_none_position(lst, value):
    none_indices = [i for i, elem in enumerate(lst) if isinstance(elem, NoneRole)]
    if none_indices:
        random_index = random.choice(none_indices)
        lst[random_index] = value
    else:
        lst.append(value)



def assign_roles(player_count):
    match player_count:
        case 4:
            return assign_roles_scenario_4()
        case 5:
            return assign_roles_scenario_5()
        case 6:
            return assign_roles_scenario_6()
        case 7:
            return assign_roles_scenario_7()
        case 8:
            return assign_roles_scenario_8()
        case other:
            raise ValueError("Invalid number of players.")

def assign_roles_scenario_4():
    player_roles = [None] * 4
    unique_indices = random.sample(range(4), 2)
    player_roles[unique_indices[0]] = Don()
    player_roles[unique_indices[1]] = Doctor()
    return player_roles

def assign_roles_scenario_5():
    player_roles = [None] * 5
    unique_indices = random.sample(range(5), 3)
    player_roles[unique_indices[0]] = Don()
    player_roles[unique_indices[1]] = Doctor()
    x = random.sample(ADDITIONAL_ROLES, 1)
    player_roles[unique_indices[2]] = x[0]
    return player_roles


def assign_roles_scenario_6():
    if random.random() < 0.5:
        player_roles = [None] * 1
        insert_none_position(player_roles, random.sample(ADDITIONAL_ROLES, 1)[0])
    else:
        player_roles = [None] * 2
    unique_indices = random.sample(range(4), 2)
    player_roles.append(Don())
    player_roles.append(Doctor())

    bad_role = random.choice([role for role in BAD_ROLES if role.get_type() != Roles.MAFIA.value and role.get_type() != Roles.DON.value])
    player_roles.append(bad_role)
    player_roles.append(Detective())
    random.shuffle(player_roles)
    return player_roles

def assign_roles_scenario_7():
    player_roles = [None]
    bad_role = random.choice([role for role in BAD_ROLES if role.get_type() != Roles.MAFIA.value and role.get_type() != Roles.DON.value])
    player_roles.append(Don())
    player_roles.append(bad_role)

    player_roles.append(Doctor())
    player_roles.append(Detective())

    neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
    print(bad_role)
    player_roles.extend(neutral_roles)
    random.shuffle(player_roles)
    return player_roles

def assign_roles_scenario_8():
    player_roles = [None]*2
    bad_role = random.choice([role for role in BAD_ROLES if role.get_type() != Roles.MAFIA.value and role.get_type() != Roles.DON.value])
    player_roles.append(Don())
    player_roles.append(bad_role)

    player_roles.append(Doctor())
    player_roles.append(Detective())

    neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
    print(bad_role)
    player_roles.extend(neutral_roles)
    random.shuffle(player_roles)
    return player_roles

# Передаем обязательно через UserState
def assign_roles(users):
    player_count = len(users)
    player_roles = assign_roles(player_count)

    for user in users:
        role_name = user.role.__class__.__name__ if user.role else "None"
        print(f"Username: {user.username}, Role: {role_name}")

# Example usage

# player_count = 6
# player_roles = assign_roles(player_count)

# users = [
#     UserState(username="Пух", user_id=1, role=player_roles[0]),
#     UserState(username="Пепук", user_id=2, role=player_roles[1]),
#     UserState(username="Паша", user_id=3, role=player_roles[2]),
#     UserState(username="Артём", user_id=4, role=player_roles[3]),
#     UserState(username="Илья", user_id=5, role=player_roles[4]),
#     UserState(username="Хтось", user_id=6, role=player_roles[5]),
# ]

# for user in users:
#     role_name = user.role.__class__.__name__ if user.role else "None"
#     print(f"Username: {user.username}, Role: {role_name}")