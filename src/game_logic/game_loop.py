from src.game_logic.role_implementations import assign
from src.game_logic import wait_until_all_users_interact_or_timeout


async def start_loop(registration_state, chat_id):
    await assign(registration_state)
    # assign_roles
    # night_roles_act
    await wait_until_all_users_interact_or_timeout(chat_id)
    # set_day
    # show_int_history
    # show_alive
    # win_check
    # vote
    # check_votes
    # vote_kill
    # set_night
    # increment_day
    pass
