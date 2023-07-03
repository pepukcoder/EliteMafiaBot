import random
import enum

from src.settings.managers.mafia_chat_config_manager import MafiaChatConfigManager
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
            case 9:
                return assign_roles_scenario_9()
            case 10:
                return assign_roles_scenario_10()
            case other:
                return assign_roles_scenario_4()
                # REWORK OTHER
                # return assign_roles_scenario_other(player_count)

    def assign_roles_scenario_4():
        player_roles = [Townie()] * 2
        player_roles.append(Don())
        player_roles.append(Doctor())

        random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_5():
        player_roles = [Townie()] * 2
        player_roles.append(Don())
        player_roles.append(Doctor())
        player_roles.append(random.choice(ADDITIONAL_ROLES))

        random.shuffle(player_roles)
        return player_roles


    def assign_roles_scenario_6():
        player_roles = [Townie()]
        player_roles.append(Don())
        bad_role = []
        mafia = MafiaChatConfigManager.get_mafia_from_config(chat_id)
        if mafia == '1to3':
            bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.DON.value])
        elif mafia == '1to4':
            player_roles.append(Townie())
        player_roles.append(bad_role)
        player_roles.append(Doctor())
        player_roles.append(Detective())
        player_roles.append(random.choice(ADDITIONAL_ROLES))

        random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_7():
        player_roles = [Townie()]
        player_roles.append(Don())
        bad_role = []
        mafia = MafiaChatConfigManager.get_mafia_from_config(chat_id)
        if mafia == '1to3':
            bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.DON.value])
        elif mafia == '1to4':
            player_roles.append(Townie())
        player_roles.append(bad_role)
        player_roles.append(Doctor())
        player_roles.append(Detective())
        neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
        player_roles.extend(neutral_roles)

        random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_8():
        player_roles = [Townie()]
        player_roles.append(Don())
        player_roles.append(Mafia())
        bad_role = []
        mafia = MafiaChatConfigManager.get_mafia_from_config(chat_id)
        if mafia == '1to3':
            if random.random() < 0.5:
                bad_role = random.choice(
                    [role for role in BAD_ROLES if int(role) != Roles.MAFIA.value and int(role) != Roles.DON.value])
            else:
                player_roles.append(Townie())
        elif mafia == '1to4':
            player_roles.append(Townie())
        player_roles.append(bad_role)
        player_roles.append(Doctor())
        player_roles.append(Detective())
        neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
        player_roles.extend(neutral_roles)

        random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_9():
        player_roles = [Townie()]*2
        player_roles.append(Don())
        player_roles.append(Mafia())
        bad_role = []
        mafia = MafiaChatConfigManager.get_mafia_from_config(chat_id)
        if mafia == '1to3':
            bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.DON.value])
        elif mafia == '1to4':
            if random.random() < 0.5:
                bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.MAFIA.value and int(role) != Roles.DON.value])
            else:
                player_roles.append(random.choice(ADDITIONAL_ROLES))
        player_roles.append(bad_role)
        player_roles.append(Doctor())
        player_roles.append(Detective())

        neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
        player_roles.extend(neutral_roles)

        random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_10():
        player_roles = [Townie()]*2
        player_roles.append(Don())
        player_roles.append(Mafia())
        bad_role = []
        mafia = MafiaChatConfigManager.get_mafia_from_config(chat_id)
        if mafia == '1to3':
            player_roles.append(Mafia())
            bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.MAFIA.value and int(role) != Roles.DON.value])
        elif mafia == '1to4':
            if random.random() < 0.5:
                bad_role = random.choice([role for role in BAD_ROLES if int(role) != Roles.MAFIA.value and int(role) != Roles.DON.value])
            else:
                player_roles.append(random.choice(ADDITIONAL_ROLES))
            player_roles.append(Townie())
        player_roles.append(bad_role)
        player_roles.append(Doctor())
        player_roles.append(Detective())

        neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
        player_roles.extend(neutral_roles)

        random.shuffle(player_roles)
        return player_roles

    def assign_roles_scenario_other(count):
        player_roles = [Don()]
        player_roles.append(Doctor())
        player_roles.append(Detective())

        # REWORK NEEDED
        bad_role = []
        mafia = MafiaChatConfigManager.get_mafia_from_config(chat_id)
        if mafia == '1to3':
            bad_count = (count // 3) - 1
            bad_role = random.sample([role for role in BAD_ROLES if int(role) != Roles.DON.value], bad_count)
        elif mafia == '1to4':
            bad_count = (count // 4) - 1
            bad_role = random.sample([role for role in BAD_ROLES if int(role) != Roles.DON.value], bad_count)
        player_roles.extend(bad_role)
        # _____________________

        neutral_roles = random.sample(ADDITIONAL_ROLES, 2)
        player_roles.extend(neutral_roles)

        random.shuffle(player_roles)
        return player_roles

    # assigning
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
