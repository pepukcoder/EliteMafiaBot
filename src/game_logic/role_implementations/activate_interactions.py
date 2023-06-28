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

    #Liar move
    try:
        liar_target_id = [record.interaction_object for record in today_int if
                          record.interaction_type == InteractionTypes.lie][0]
    except IndexError:
        liar_target_id = []

    # Users to kill
    try:
        users_to_kill = [record.interaction_object for record in today_int if
                         record.interaction_type == InteractionTypes.kill]
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
            await bot.send_message(chat_id=detective, text=f"{detective_check_user_id} - 👨🏼Мирный житель")
        else:
            # send detective real role
            detective = get_user_id_by_role(chat_id, Roles.DETECTIVE)
            print(detective)
            await bot.send_message(chat_id=detective, text=f"{detective_check_user_id} - {str(get_role_by_user_id(chat_id=chat_id, user_id=detective_check_user_id))}")
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
        await bot.send_message(chat_id=omega_target_id, text=f"У тебя спиздили роль на следующую ночь, поэтому ты не сможешь ничего делать")
        await bot.send_message(chat_id=omega, text=f"Ты успешно спиздил роль. Теперь ты - {str(get_role_by_user_id(chat_id, omega))}")

    except:
        omega_target_id = []
    try:
        users_to_kill.remove(doctor_target_id)
    except ValueError:
        print('#докеблан')

    if len(users_to_kill) == 0:
        await bot.send_message(chat_id=chat_id,
                               text=f"Сегодня был ёбнут... А стоп... *Никто небыл ёбнут!*\n#донгандон", parse_mode="Markdown")
    for usr in users_to_kill:
        print(usr)
        await bot.send_message(chat_id=chat_id,
                               text=f"Сегодня был ёбнут *{usr}*\n#донгандон", parse_mode="Markdown")
    Delete.delete_all_elements_by_id(chat_id=chat_id, user_ids=users_to_kill)


