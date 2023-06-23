import asyncio

from src.game_logic.waiting_strategies import Strategy
from src.state import State
from src.state.enums import Roles


class WaitingForInteractionStrategy(Strategy):
    async def wait(self, game_chat_id: int):
        timer = 0
        timer_step = 5
        while True:
            await asyncio.sleep(timer_step)
            timer += timer_step

            state = State()
            game = state.get_game_or_none(game_chat_id)

            if game is None:
                raise ValueError("Game can't be None")

            users_with_role = [user for user in game.users if user.role.get_type() is not Roles.TOWNIE]
            this_day_interactions = [record for record in game.interaction_history if record.day == game.day]

            # if one user do one interaction by night then number of interactions == number of users with role
            if len(users_with_role) == len(this_day_interactions):
                return

            if timer >= 60:
                return
