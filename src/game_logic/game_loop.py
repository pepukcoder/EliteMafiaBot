from src.game_logic.create_game_state import create_game_state
from src.game_logic.role_implementations import assign
from src.game_logic.sending_strategies import SendRoleNameMessagesStrategy, SendInteractiveMessagesStrategy
from aiogram import Bot

from src.game_logic.waiting_context import WaitingContext
from src.game_logic.waiting_strategies import WaitingForInteractionStrategy
#Вот это как временная хуйня онли, передавай в start_loop бота крч. Як Ілля, жорстко плюсую
from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
# --------

from src.game_logic.sending_strategies import EmptyArrayAndDeleteRegistrationMessage
from src.functions.show_alive import show_alive

async def start_loop(chat_id):
    #create_game_state
    create_game_state(chat_id)

    #assign_roles
    await assign(chat_id) 

    #send roles to pm
    await SendRoleNameMessagesStrategy().send(chat_id, bot)
    #show alive users
    show_alive(chat_id, bot)
    #empty array and delete reg message
    await EmptyArrayAndDeleteRegistrationMessage().delete(chat_id, bot)
    #send interaction keyboard. Note: This must be called INSIDE the game loop
    await SendInteractiveMessagesStrategy().send(chat_id, bot)

    # night_roles_act
    # wait_until_all_users_interact_or_timeout
    waiting_context = WaitingContext(WaitingForInteractionStrategy())
    await waiting_context.wait(chat_id)

    # set_day
    # show_interaction_history
    # show_alive
    # win_check
    # vote
    # check_votes
    # vote_kill
    # set_night
    # increment_day
    pass
