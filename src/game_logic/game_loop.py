from src.game_logic.role_implementations import assign
from src.game_logic import wait_until_all_users_interact_or_timeout
from src.game_logic.sending_strategies import SendRoleNameMessagesStrategy
from aiogram import Bot

#Вот это как временная хуйня онли, передавай в start_loop бота крч
from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
# --------
send_role = SendRoleNameMessagesStrategy()

async def start_loop(chat_id):
    await assign(chat_id) # assign_roles
    await send_role.send(chat_id, bot)
    # night_roles_act
    # wait_until_all_users_interact_or_timeout(chat_id)
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
