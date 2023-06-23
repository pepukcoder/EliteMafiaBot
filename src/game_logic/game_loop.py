from src.game_logic.role_implementations import assign
from src.game_logic.waiting_context import WaitingContext
from src.game_logic.waiting_strategies import WaitingForInteractionStrategy


async def start_loop(registration_state, chat_id):
    await assign(registration_state)
    # assign_roles
    # night_roles_act
    waiting_context = WaitingContext(WaitingForInteractionStrategy())
    await waiting_context.wait(chat_id)
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
