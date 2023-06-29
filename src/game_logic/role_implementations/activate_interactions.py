from aiogram import Bot

from src.game_logic.role_implementations import Townie
from src.misc import TgKeys
from src.state.enums import Roles
from src.functions import get_user_id_by_role, get_role_by_user_id, change_user_role
from src.functions.delete_element_by_id import Delete

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

from src.state import State
from src.state.enums import InteractionTypes
from collections import Counter


def remove_duplicates(lst):
    return list(set(lst))


async def check_switch_back(chat_id: int):
    state = State()
    game = state.games[chat_id]
    previous_day = game.day - 1
    prev_day_interactions = [record for record in game.interaction_history if record.day == previous_day]

    for interaction in prev_day_interactions:
        if interaction.interaction_type == 10:
            snatched_role = get_role_by_user_id(chat_id, interaction.interaction_subject)
            townie = get_role_by_user_id(chat_id, interaction.interaction_object)
            change_user_role(chat_id, interaction.interaction_subject, townie)
            await bot.send_message(chat_id=interaction.interaction_subject,
                                   text=f"Тебя раскрыли и отпиздили, теперь ты ты - {str(get_role_by_user_id(chat_id, interaction.interaction_subject))}")
            change_user_role(chat_id, interaction.interaction_object, snatched_role)
            await bot.send_message(chat_id=interaction.interaction_object,
                                   text=f"Омега был успешно опущен, теперь ты снова {str(get_role_by_user_id(chat_id, interaction.interaction_object))}")

        else:
            return


def get_name_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.first_name


async def activate_interactions(chat_id: int) -> None:
    state = State()
    game = state.games[chat_id]

    today_int = [rec for rec in game.interaction_history if rec.day == game.day]

    # Whore move:
    try:
        whore_target_id = [record.interaction_subject for record in today_int if
                           record.interaction_type == InteractionTypes.fuck_whore]

        today_int = [record for record in today_int if
                     record.interaction_object is not whore_target_id]
    except IndexError:
        whore_target_id = []

    # Liar move
    try:
        liar_target_id = [record.interaction_object for record in today_int if
                          record.interaction_type == InteractionTypes.lie][0]
    except IndexError:
        liar_target_id = []

    # Users to kill
    try:
        users_to_kill = [record.interaction_object for record in today_int
                         if record.interaction_type == InteractionTypes.kill]

    except:
        users_to_kill = []

    # Mafia move
    try:
        mafia_targets = [record.interaction_object for record in today_int if
                         record.interaction_type == InteractionTypes.don_vote_kill or
                         record.interaction_type == InteractionTypes.mafia_vote_kill]
    except IndexError:
        mafia_targets = []

    mafia_target_counter = Counter(mafia_targets)
    most_common_mafia_targets = mafia_target_counter.most_common()

    try:
        # if two or more, most voted targets have same vote quantity
        if most_common_mafia_targets[0][1] == most_common_mafia_targets[1][1]:
            # kill don's target
            don_target = [record.interaction_object for record in today_int if
                          record.interaction_type == InteractionTypes.don_vote_kill][0]
            users_to_kill.append(don_target)

        else:
            # kill most voted target
            users_to_kill.append(most_common_mafia_targets[0][0])
    except:
        try:
            users_to_kill.append(most_common_mafia_targets[0][0])
        except:
            print('huy')
    try:
        # Detective check move
        detective_check_record = [record for record in today_int if
                                  record.interaction_type == InteractionTypes.check][0]

        detective_check_user_id = detective_check_record.interaction_object
        detective_check_target_id = detective_check_record.interaction_subject

        # TODO: implementation
        if detective_check_target_id == liar_target_id:
            # send fake bad role
            detective = get_user_id_by_role(chat_id, Roles.DETECTIVE)
            print(detective)
            await bot.send_message(chat_id=detective,
                                   text=f"{get_name_by_user_id(chat_id, detective_check_user_id)} - 👨🏼Мирный житель")
            await bot.send_message(chat_id=detective_check_user_id, text=f"Тебя чекал коммисар")
        else:
            # send detective real role
            detective = get_user_id_by_role(chat_id, Roles.DETECTIVE)
            print(detective)
            await bot.send_message(chat_id=detective,
                                   text=f"{get_name_by_user_id(chat_id, detective_check_user_id)} - {str(get_role_by_user_id(chat_id=chat_id, user_id=detective_check_user_id))}")
            await bot.send_message(chat_id=detective_check_user_id, text=f"Тебя чекал коммисар")
            pass
    except:
        detective_check_record = []

    # Doctor move
    try:
        doctor_target_id = [record.interaction_object for record in today_int if
                            record.interaction_type == InteractionTypes.heal][0]
    except IndexError:
        doctor_target_id = []

    # TODO: OMEGA, INFORMANT, LAWYER

    try:
        omega_target_id = [record.interaction_object for record in today_int if
                           record.interaction_type == InteractionTypes.switch][0]
        print(omega_target_id)
        omega = get_user_id_by_role(chat_id, Roles.OMEGA)
        temp_role = get_role_by_user_id(chat_id, omega_target_id)
        change_user_role(chat_id, omega, temp_role)
        change_user_role(chat_id, omega_target_id, Townie())
        await bot.send_message(chat_id=omega_target_id, text=f"Омега спиздил твою роль, теперь ты сосёшь хуйца")
        await bot.send_message(chat_id=omega_target_id,
                               text=f"У тебя спиздили роль на следующую ночь, поэтому ты не сможешь ничего делать")
        await bot.send_message(chat_id=omega,
                               text=f"Ты успешно спиздил роль. Теперь ты - {get_role_by_user_id(chat_id, omega)}")

        await check_switch_back(chat_id)
    except:
        omega_target_id = []
        await check_switch_back(chat_id)

    try:
        informant_target_id = [record.interaction_object for record in today_int if
                               record.interaction_type == InteractionTypes.podsos][0]

        try:
            if informant_target_id == get_user_id_by_role(chat_id, Roles.DETECTIVE):
                await bot.send_message(chat_id=get_user_id_by_role(chat_id, Roles.DON),
                                       text=f"{get_name_by_user_id(chat_id, informant_target_id)} - {get_role_by_user_id(chat_id, informant_target_id)}")
                await bot.send_message(chat_id=get_user_id_by_role(chat_id, Roles.INFORMANT),
                                       text=f"{get_name_by_user_id(chat_id, informant_target_id)} - {get_role_by_user_id(chat_id, informant_target_id)}")
            else:
                await bot.send_message(chat_id=get_user_id_by_role(chat_id, Roles.DON),
                                       text=f"{get_name_by_user_id(chat_id, informant_target_id)} - {get_role_by_user_id(chat_id, informant_target_id)}")
        except:
            pass
    except IndexError:
        informant_target_id = []

    remove_duplicates(users_to_kill)

    try:
        users_to_kill.remove(doctor_target_id)
    except:
        print('Doc didnt choose')
    if len(users_to_kill) == 0:
        await bot.send_message(chat_id=chat_id,
                               text=f"🤷‍♂️ Удивительно, но *никто небыл убит!*\n#донгандон", parse_mode="Markdown")

        for el in users_to_kill:
            await bot.send_message(chat_id=el,
                                   text=f"🤷‍♂️ Тебя пытались убить, но ты выжил.", parse_mode="Markdown")
    for usr in users_to_kill:
        print(usr)
        await bot.send_message(chat_id=chat_id,
                               text=f"Сегодня был ёбнут *{get_name_by_user_id(chat_id, usr)}*\n#донгандон",
                               parse_mode="Markdown")

        for el in users_to_kill:
            await bot.send_message(chat_id=el,
                                   text=f"Тебя убили :(\n Напиши предсмертное сообщение:", parse_mode="Markdown")

    Delete.delete_all_elements_by_id(chat_id=chat_id, user_ids=users_to_kill)
