from src.state import State
from aiogram import Bot
from src.state.enums import InteractionTypes

from src.misc import TgKeys
from src.functions.get_user_firstname_by_id import GetFirstName

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

from src.functions.delete_element_by_id import Delete


async def check_interaction_conflicts(chat_id):
    state = State()
    game = state.games[chat_id]
    this_day_interactions = [record for record in game.interaction_history if record.day == game.day]
    print(game.users)

    # maf_int = [a for a in today if get_role_by_user_id(chat_id, a.interaction_object) == Roles.MAFIA]
    print(this_day_interactions)
    kill_int = [record for record in this_day_interactions if record.interaction_type == InteractionTypes.don_vote_kill]
    heal_int = [record for record in this_day_interactions if record.interaction_type == InteractionTypes.heal]
    # det_int = [a for a in today if get_role_by_user_id(chat_id, a.interaction_object) == Roles.DETECTIVE]
    # liar_int = [a for a in today if get_role_by_user_id(chat_id, a.interaction_object) == Roles.LIAR]
    # inf_int = [a for a in today if get_role_by_user_id(chat_id, a.interaction_object) == Roles.INFORMANT]
    print(kill_int, heal_int)
    for kill_record, heal_record in zip(kill_int, heal_int):
        if kill_record.interaction_object == heal_record.interaction_object:
            await bot.send_message(chat_id=chat_id,
                                   text="🤷‍Удивительно, но этой ночью все выжили\n#доккрос\n#донгандон")
        else:
            Delete.delete_element_by_id(chat_id=chat_id, user_id=kill_record.interaction_object)
            await bot.send_message(chat_id=chat_id,
                                   text=f"Сегодня был жёстко убит {GetFirstName.get_user_firstname_by_id(chat_id=chat_id, user_id=kill_record.interaction_object)}...\n#донгандон")

