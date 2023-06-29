import random
import enum

from src.state.enums import Roles
from src.game_logic.role_implementations import Don, Mafia, Liar, Informant, Doctor, Detective, Whore, Omega, Lawyer, Alfa, Townie
from src.state import UserState
from src.state import State

state = State()

BAD_ROLES = [Don(), Mafia(), Liar(), Informant()]
ADDITIONAL_ROLES = [Whore(), Omega(), Lawyer(), Alfa()]
GOOD_ROLES = [Detective(), Doctor()]

async def assign(chat_id):
    state = State()

    def insert_townie_position(lst, value):
        townie_indices = [i for i, elem in enumerate(lst) if isinstance(elem, Townie)]
        if townie_indices:
            random_index = random.choice(townie_indices)
            lst[random_index] = value

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
                return assign_roles_scenario_8plus(player_count)
                # raise ValueError("Invalid number of players.")

    def assign_roles_scenario_4():
        player_roles = [Townie()] * 4
        unique_indices = random.sample(range(4), 2)
        player_roles[unique_indices[0]] = Don()
        player_roles[unique_indices[1]] = Doctor()
        return player_roles

    def assign_roles_scenario_5():
        player_roles = [Townie()] * 5
        unique_indices = random.sample(range(5), 3)
        player_roles[unique_indices[0]] = Don()
        player_roles[unique_indices[1]] = Doctor()
        x = random.sample(ADDITIONAL_ROLES, 1)
        player_roles[unique_indices[2]] = x[0]
        return player_roles


    def assign_roles_scenario_6():
        if random.random() < 0.5:
            player_roles = [Townie()] * 1
            player_roles.append(random.choice(ADDITIONAL_ROLES))
        else:
            player_roles = [Townie()] * 2
        unique_indices = random.sample(range(4), 2)
        player_roles.append(Don())
        player_roles.append(Doctor())

        bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.MAFIA.value and int(role) != Roles.DON.value])
        player_roles.append(bad_role)
        player_roles.append(Detective())
        random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_7():
        player_roles = [Townie()]
        bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.DON.value])
        player_roles.append(Don())
        player_roles.append(bad_role)

        player_roles.append(Doctor())
        player_roles.append(Detective())

        neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
        player_roles.extend(neutral_roles)
        random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_8():
        player_roles = [Doctor()]
        player_roles.append(Don())
        #player_roles = [Townie()]*2
        #bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.DON.value])
        #player_roles.append(Don())
        #player_roles.append(bad_role)

        #player_roles.append(Doctor())
        #player_roles.append(Detective())

        #neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
        #player_roles.extend(neutral_roles)
        #random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_8plus(count):
        player_roles = [Townie()]*(count-6)
        bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.DON.value])
        player_roles.append(Don())
        player_roles.append(bad_role)

        player_roles.append(Doctor())
        player_roles.append(Detective())

        neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
        player_roles.extend(neutral_roles)
        random.shuffle(player_roles)
        return player_roles

    try:
        user_dict = state.registrations[chat_id]

        player_count = len(user_dict.users)
        player_roles = assign_roles(player_count)

        first_names = [item.first_name for item in user_dict.users.values()]
        links = [item.link for item in user_dict.users.values()]
        users = []
        initial_roles = []
        for idx, x in enumerate(user_dict.users):
            users.append(UserState(first_name=first_names[idx],
                                   user_id=list(user_dict.users.keys())[idx],
                                   role=player_roles[idx],
                                   link=links[idx]))

            initial_roles.append(UserState(first_name=first_names[idx],
                                   user_id=list(user_dict.users.keys())[idx],
                                   role=player_roles[idx],
                                   link=links[idx]))

        try:
            state.games[chat_id].users = users
            state.games[chat_id].initial_roles = initial_roles
        except KeyError:
            print(f"Game {chat_id} not found")

    except KeyError:
        print(f"Registration {chat_id} not found")
