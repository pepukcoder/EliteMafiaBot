from src.functions import get_user_firstname_by_id
from src.state import State
from aiogram import Bot
from src.state.enums import InteractionTypes

from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

from src.functions.delete_element_by_id import Delete
from src.settings.main import get_language

async def interact(chat_id):
    state = State()
    game = state.games[chat_id]
    today_int = [rec for rec in game.interaction_history if rec.day == game.day]
    print('TODAY')
    print(today_int)

    # maf_int = [a for a in today if get_role_by_user_id(chat_id, a.interaction_object) == Roles.MAFIA]
    kill_int = [rec for rec in today_int if rec.interaction_type == InteractionTypes.don_vote_kill]
    # kill_int.extend([rec for rec in today_int if rec.interaction_type == InteractionTypes.kill])

    whore_int = [rec for rec in today_int if rec.interaction_type == InteractionTypes.fuck_whore]
    liar_int = [rec for rec in today_int if rec.interaction_type == InteractionTypes.lie]
    det_int = [rec for rec in today_int if rec.interaction_type == InteractionTypes.check]
    heal_int = [rec for rec in today_int if rec.interaction_type == InteractionTypes.heal]
    # liar_int = [a for a in today if get_role_by_user_id(chat_id, a.interaction_object) == Roles.LIAR]
    # inf_int = [a for a in today if get_role_by_user_id(chat_id, a.interaction_object) == Roles.INFORMANT]
    print('DON')
    print(whore_int)
    print('WHORE')
    print(whore_int)
    print('LIAR')
    print(liar_int)
    for kill_rec, heal_rec in zip(kill_int, heal_int):
        if kill_rec.interaction_object == heal_rec.interaction_object:
            await bot.send_message(chat_id=chat_id,
                                   text=f"{get_language(chat_id)['killed_nobody']}\n#доккрос\n#донгандон")
        else:
            Delete.delete_element_by_id(chat_id=chat_id, user_id=kill_rec.interaction_object)
            await bot.send_message(chat_id=chat_id,
                                   text=f"{get_language(chat_id)['killed']} {get_user_firstname_by_id(chat_id=chat_id, user_id=kill_rec.interaction_object)}...\n#донгандон")


    for whore_rec, all_rec in zip(whore_int, today_int):
        if whore_rec.interaction_object == all_rec.interaction_subject:
            print('whore blocked')

    for liar_rec, det_rec in zip(liar_int, det_int):
        if liar_rec.interaction_object == det_rec.interaction_object:
            print('liar faked role')