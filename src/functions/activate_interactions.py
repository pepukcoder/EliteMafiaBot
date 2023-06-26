from src.state import State
from src.state.enums import InteractionTypes
from collections import Counter


def activate_interactions(chat_id: int) -> None:
    state = State()
    game = state.games[chat_id]

    today_int = [rec for rec in game.interaction_history if rec.day == game.day]

    # Whore move:
    whore_target_id = [record.interaction_subject for record in today_int if
                       record.interaction_type is InteractionTypes.fuck_whore][0]

    today_int = [record for record in today_int if
                 record.interaction_object is not whore_target_id]

    # Liar move
    liar_target_id = [record.interaction_object for record in today_int if
                      record.interaction_type is InteractionTypes.lie][0]

    # Users to kill
    users_to_kill = [record.interaction_object for record in today_int if
                     record.interaction_type is InteractionTypes.kill]

    # Mafia move
    mafia_targets = [record.interaction_object for record in today_int if
                     record.interaction_type is InteractionTypes.don_vote_kill or
                     record.interaction_type is InteractionTypes.mafia_vote_kill]

    mafia_target_counter = Counter(mafia_targets)
    most_common_mafia_targets = mafia_target_counter.most_common()

    # if two or more, most voted targets have same vote quantity
    if most_common_mafia_targets[0][1] is most_common_mafia_targets[1][1]:
        # kill don's target
        don_target = [record.interaction_object for record in today_int if
                      record.interaction_type is InteractionTypes.don_vote_kill][0]
        users_to_kill.append(don_target)
    else:
        # kill most voted target
        users_to_kill.append(most_common_mafia_targets[0][0])

    # Detective check move
    detective_check_record = [record for record in today_int if
                              record.interaction_type is InteractionTypes.check][0]

    detective_check_user_id = detective_check_record.interaction_subject
    detective_check_target_id = detective_check_record.interaction_subject

    # TODO: implementation
    if detective_check_target_id == liar_target_id:
        # send fake bad role
        pass
    else:
        # send detective real role
        pass

    # Doctor move
    doctor_target_id = [record.interaction_object for record in today_int if
                        record.interaction_type is InteractionTypes.heal][0]

    try:
        users_to_kill.remove(doctor_target_id)
    except ValueError:
        pass



    # TODO: OMEGA, INFORMANT, LAWYER
