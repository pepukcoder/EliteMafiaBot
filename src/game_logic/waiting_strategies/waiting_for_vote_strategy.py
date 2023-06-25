import asyncio

from src.game_logic.waiting_strategies import Strategy
from src.state import State, VoteState
from src.state.enums import Roles


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
                    return
                    await asyncio.sleep(15)

                if timer >= 60:
                    return
            except KeyError:
                print(f"Game {game_chat_id} not found")