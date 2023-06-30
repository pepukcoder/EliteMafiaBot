import asyncio

from src.functions.remove_game_state import remove_game_state
from src.game_logic.create_game_state import create_game_state
from src.game_logic.role_implementations import assign, activate_interactions
from src.game_logic.sending_context import SendingContext
from src.game_logic.sending_strategies import SendRoleNameMessagesStrategy, SendInteractiveMessagesStrategy, \
    SendVotingMessages, SendMafiaParticipants
from aiogram import Bot
from src.misc import set_night, set_day
from src.game_logic.waiting_context import WaitingContext
from src.game_logic.waiting_strategies import WaitingForInteractionStrategy, WaitingForVoteStrategy

from src.functions import show_alive, delete_reg, increment_day, vote_lynch, win_check, announce_vote, Delete, \
    clean_voting
from src.state import State

# Вот это как временная хуйня онли, передавай в start_loop бота крч. Як Ілля, жорстко плюсую
# Как пепуку, мне похуй, я просто делаю таски, плюсую на всякий
# Как паша, хочу сказать, что это полная хуйня. И кстати, прошло уже сколько ебать дней а так нихуя. Привет из 29.06.2023, внуки, если вы это читаете, я вас люблю, а еще знайте, что в детстве Паша пиздился в гаражах за бутылку пива, так что не всегда его нужно слушать ибо он еблан. Передаю привет внучкам короче, а моим деткам на будущее советую чтоб не слушали этого старого петуха пердуна, кстати, если это читают дети или внуки пепука и ильи я желаю им всего найлучшего.
from src.misc import TgKeys
from src.state import State

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML',proxy="http://proxy.server:3128")
# --------

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
    # send mafia participants if they are
    sending_context = SendingContext(SendMafiaParticipants())
    await sending_context.send_mafia(chat_id, bot)

    playing = True

    while playing:
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

        # set day
        await Delete.delete_all_interaction_keyboards(chat_id, bot)
        await increment_day(chat_id)
        await set_day(chat_id, bot)
        await show_alive(chat_id, bot)

        # win check
        playing = await win_check(chat_id, bot)
        if not playing:
            break

        # vote
        await asyncio.sleep(40)
        await announce_vote(chat_id, bot)
        sending_context = SendingContext(SendVotingMessages())
        await sending_context.send_voting(chat_id, bot)

        waiting_context = WaitingContext(WaitingForVoteStrategy())
        await waiting_context.wait(chat_id)

        # check voting and kill
        await vote_lynch(chat_id, bot)

        await Delete.delete_all_keyboards(chat_id, bot)

        clean_voting(chat_id)

        # win check 2
        playing = await win_check(chat_id, bot)

    # remove game_state
    remove_game_state(chat_id)