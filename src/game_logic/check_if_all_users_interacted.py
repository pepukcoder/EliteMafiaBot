import asyncio

from src.state import State
from src.state.enums import Roles

users_interacted_event = asyncio.Event()
timeout_event = asyncio.Event()


async def check_interactions_task(chat_id: int):
    while True:
        # if time is out then skip interaction
        if timeout_event.is_set():
            return

        await asyncio.sleep(5)

        state = State()
        game = list(filter(lambda x: x.chat_id == chat_id, state.games))[0]

        users_with_role = [user for user in game.users if user.role.get_type() is not Roles.TOWNIE]
        this_day_interactions = [record for record in game.interaction_history if record.day == game.day]

        # if one user do one interaction by night then number of interactions == number of users with role
        if len(users_with_role) == len(this_day_interactions):
            users_interacted_event.set()
            return


async def timer_task():
    i = 0
    while True:
        # If all users already interacted then skip timer
        if users_interacted_event.is_set():
            return

        await asyncio.sleep(5)

        i += 1
        if i >= 12:  # 12 * 5 = 60 sec
            timeout_event.set()
            return


def wait_until_all_users_interact_or_timeout(chat_id: int):
    loop = asyncio.get_event_loop()
    tasks = []
    tasks[0] = loop.create_task(timer_task())
    tasks[1] = loop.create_task(check_interactions_task(chat_id))
    loop.run_until_complete(asyncio.wait(tasks))
