import asyncio

from src.game_logic.waiting_strategies import Strategy
from src.state import State
from src.functions import end_voting


class WaitingForVoteStrategy(Strategy):

    async def wait(self, game_chat_id: int):
        timer = 0
        timer_step = 5
        while True:
            await asyncio.sleep(timer_step)
            timer += timer_step

            state = State()
            try:
                game = state.games[game_chat_id]

                
                vote_objects = [vote.vote_object for vote in state.games[game_chat_id].votes]
                print(vote_objects)

                # if one user do one interaction by night then number of interactions == number of users with role
                if len(game.users) == len(vote_objects):
                    await end_voting(game_chat_id)
                    await asyncio.sleep(15)
                    return

                if timer >= 60:
                    await end_voting(game_chat_id)
                    await asyncio.sleep(15)
                    return
            except KeyError:
                print(f"Game {game_chat_id} not found")