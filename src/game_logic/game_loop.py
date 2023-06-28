import asyncio

from src.game_logic.create_game_state import create_game_state
from src.game_logic.role_implementations import assign, activate_interactions
from src.game_logic.sending_context import SendingContext
from src.game_logic.sending_strategies import SendRoleNameMessagesStrategy, SendInteractiveMessagesStrategy, \
    SendVotingMessages
from aiogram import Bot
from src.misc import set_night, set_day
from src.game_logic.waiting_context import WaitingContext
from src.game_logic.waiting_strategies import WaitingForInteractionStrategy, WaitingForVoteStrategy

# Вот это как временная хуйня онли, передавай в start_loop бота крч. Як Ілля, жорстко плюсую
from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
# --------

from src.functions import show_alive, delete_reg
from src.functions.increase_day import increment_day


async def start_loop(chat_id):
    # create_game_state
    create_game_state(chat_id)

    # assign_roles
    await assign(chat_id)
    await delete_reg(chat_id, bot)

    sending_context = SendingContext(SendRoleNameMessagesStrategy())
    # send roles to pm
    await sending_context.send(chat_id, bot)

    while True:
        # set night
        await set_night(chat_id, bot)
        # show alive users
        await show_alive(chat_id, bot)
        # empty array and delete reg message
        # send interaction keyboard. Note: This must be called INSIDE the game loop
        sending_context.strategy = SendInteractiveMessagesStrategy()
        await sending_context.send(chat_id, bot)

        # night_roles_act
        # wait_until_all_users_interact_or_timeout
        waiting_context = WaitingContext(WaitingForInteractionStrategy())
        await waiting_context.wait(chat_id)
        await activate_interactions(chat_id)
        await set_day(chat_id, bot)

        # set day
        await increment_day(chat_id)
        # check for ineraction conflicts
        # show_alive
        await show_alive(chat_id, bot)
        # show_interaction_history
        # win_check

        # vote
        # await asyncio.sleep(30)
        sending_context = SendingContext(SendVotingMessages())
        await sending_context.send_voting(chat_id, bot)

        waiting_context = WaitingContext(WaitingForVoteStrategy())
        await waiting_context.wait(chat_id)

        # check_votes
        # vote_kill
        # set_night
        # increment_day
