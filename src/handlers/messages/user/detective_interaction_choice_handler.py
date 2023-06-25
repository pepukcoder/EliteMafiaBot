from aiogram import Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified

from src.game_logic.role_implementations import DetectiveLogic


def register_detective_interaction_choice_handler(dp: Dispatcher):
    @dp.callback_query_handler(filters.Regexp(r'detectivecheck_\d*'))
    async def detective_interaction_choice_check_handler(call: CallbackQuery):
        chat_id = call.data.split("_")[1]

        try:
            await call.message.edit_text(text=DetectiveLogic.get_check_message(), reply_markup=DetectiveLogic.get_check_kb(int(chat_id)))
        except MessageNotModified:
            await call.message.edit_text("Ты уже проверил всех игроков!")



    @dp.callback_query_handler(filters.Regexp(r'detectivekill_\d*'))
    async def detective_interaction_choice_kill_handler(call: CallbackQuery):
        chat_id = call.data.split("_")[1]

        try:
            await call.message.edit_text(text=DetectiveLogic.get_kill_message(), reply_markup=DetectiveLogic.get_kill_kb(int(chat_id)))
        except MessageNotModified:
            await call.message.edit_text("Ты уже убил всех игроков. Странно, что ты видишь это сообщение")
