from aiogram import Dispatcher, Bot
from aiogram.dispatcher import filters
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified

from src.functions import get_role_by_user_id
from src.game_logic.role_implementations import DetectiveLogic
from src.misc import TgKeys
from src.settings import get_language
from src.state import State, InteractionHistoryRecord
from src.state.enums import Roles, InteractionTypes

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_detective_interaction_choice_handler(dp: Dispatcher):
    @dp.callback_query_handler(filters.Regexp(r'detectivecheck_\d*'))
    async def detective_interaction_choice_check_handler(call: CallbackQuery):
        await bot.answer_callback_query(call.id)
        chat_id = call.data.split("_")[1]
        try:
            await call.message.edit_text(text=DetectiveLogic.get_check_message(int(chat_id)), reply_markup=DetectiveLogic.get_check_kb(int(chat_id)))
            await bot.send_message(chat_id=int(chat_id),
                                   text=f"{get_role_by_user_id(chat_id=int(chat_id),user_id=int(call.from_user.id)).get_str(chat_id)} {get_language(int(chat_id))['search']}...")
        except MessageNotModified:
            await call.message.edit_text(get_language(int(chat_id))['all_checked'])

    @dp.callback_query_handler(filters.Regexp(r'detectivekill_\d*'))
    async def detective_interaction_choice_kill_handler(call: CallbackQuery):
        await bot.answer_callback_query(call.id)
        chat_id = call.data.split("_")[1]

        try:
            await call.message.edit_text(text=DetectiveLogic.get_kill_message(int(chat_id)),
                                         reply_markup=DetectiveLogic.get_kill_kb(int(chat_id)))
            await bot.send_message(chat_id=int(chat_id),
                                   text=f"{get_role_by_user_id(chat_id=int(chat_id),user_id=int(call.from_user.id)).get_str(chat_id)} {get_language(int(chat_id))['pistolet']}...")
        except MessageNotModified:
            await call.message.edit_text("Ты уже убил всех игроков. Странно, что ты видишь это сообщение")

    @dp.callback_query_handler(regexp="detectiveskip_(\-?\d+)")
    async def skip_handler(call: CallbackQuery):
        state = State()
        skip_text, chat_id = call.data.split("_")
        user_id = call.from_user.id
        day = state.games[int(chat_id)].day
        state.games[int(chat_id)].interaction_history.append(InteractionHistoryRecord(InteractionTypes.nothing,
                                                                                      0,
                                                                                      user_id,
                                                                                      day))
        await call.message.answer(get_language(int(chat_id))['skipped'])
        await bot.send_message(chat_id=int(chat_id),
                               text=f"{get_role_by_user_id(chat_id=int(chat_id), user_id=user_id).get_str(chat_id)} {get_language(int(chat_id))['kukold_huy']}")
        await call.message.delete()
