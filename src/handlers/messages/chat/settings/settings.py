from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Dispatcher
from src.settings.main import get_language, set_settings, get_mafia_by_chat_id, get_language_by_chat_id


def register_settings_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['settings'])
    async def settings(message: types.Message):
        chat_id = message.chat.id

        msg = await message.reply(get_language(chat_id)['language'])

        inline = InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(text=get_language(chat_id)['lang'], callback_data="language"),
            InlineKeyboardButton(text=get_language(chat_id)['maf'], callback_data="mafia_quantity")
        )
        await msg.edit_text(get_language(chat_id)['settings'], reply_markup=inline)

    @dp.callback_query_handler(lambda c: c.data == 'language')
    async def handle_button_click(callback_query: types.CallbackQuery):
        lang_1 = InlineKeyboardButton(text="Русский🇷🇺", callback_data="select_ru")
        lang_2 = InlineKeyboardButton(text="Українська🇺🇦", callback_data="change_ua")
        lang_3 = InlineKeyboardButton(text="English🏳️‍🌈", callback_data="change_en")
        inline = InlineKeyboardMarkup(row_width=1).add(lang_1, lang_2, lang_3)
        message = callback_query.message
        await message.edit_reply_markup(inline)

    # mafia_quantity change
    @dp.callback_query_handler(lambda c: c.data == 'mafia_quantity')
    async def handle_button_click(callback_query: types.CallbackQuery):
        one_per_3 = InlineKeyboardButton(text="1/3", callback_data="change_1_3")
        one_per_4 = InlineKeyboardButton(text="1/4", callback_data="change_1_4")
        inline = InlineKeyboardMarkup(row_width=1).add(one_per_3, one_per_4)
        message = callback_query.message
        await message.edit_reply_markup(inline)

    @dp.callback_query_handler(lambda c: c.data == 'change_1_3')
    async def handle_button_click(callback_query: types.CallbackQuery):
        # Extract the message and chat IDs
        message = callback_query.message
        await message.delete()
        chat_id = message.chat.id

        # Send a response message
        set_settings(chat_id, str(get_language_by_chat_id(chat_id)), '1to3')
        await message.answer(text=get_language(chat_id)['maf_changed'])

    @dp.callback_query_handler(lambda c: c.data == 'change_1_4')
    async def handle_button_click(callback_query: types.CallbackQuery):
        # Extract the message and chat IDs
        message = callback_query.message
        await message.delete()
        chat_id = message.chat.id

        # Send a response message
        set_settings(chat_id, str(get_language_by_chat_id(chat_id)), '1to4')
        await message.answer(text=get_language(chat_id)['maf_changed'])

    # lang change
    @dp.callback_query_handler(lambda c: c.data == 'select_ru')
    async def handle_button_click(callback_query: types.CallbackQuery):
        lang_1 = InlineKeyboardButton(text="Русский🇷🇺", callback_data="change_ru")
        lang_2 = InlineKeyboardButton(text="Русский ёбнутый🇷🇺", callback_data="change_ru_mod")
        inline = InlineKeyboardMarkup(row_width=1).add(lang_1, lang_2)
        message = callback_query.message
        await message.edit_reply_markup(inline)

    @dp.callback_query_handler(lambda c: c.data == 'change_ru')
    async def handle_button_click(callback_query: types.CallbackQuery):
        # Extract the message and chat IDs
        message = callback_query.message
        await message.delete()
        chat_id = message.chat.id

        # Send a response message
        set_settings(chat_id, 'ru', str(get_mafia_by_chat_id(chat_id)))
        await message.answer(text=get_language(chat_id)['lang_changed'])

    @dp.callback_query_handler(lambda c: c.data == 'change_ru_mod')
    async def handle_button_click(callback_query: types.CallbackQuery):
        # Extract the message and chat IDs
        message = callback_query.message
        await message.delete()
        chat_id = message.chat.id

        # Send a response message
        set_settings(chat_id, 'ru_mod', str(get_mafia_by_chat_id(chat_id)))
        await message.answer(text=get_language(chat_id)['lang_changed'])

    @dp.callback_query_handler(lambda c: c.data == 'change_ua')
    async def handle_button_click(callback_query: types.CallbackQuery):
        # Extract the message and chat IDs
        message = callback_query.message
        await message.delete()
        chat_id = message.chat.id

        # Send a response message
        set_settings(chat_id, 'uk', str(get_mafia_by_chat_id(chat_id)))
        await message.answer(text=get_language(chat_id)['lang_changed'])

    @dp.callback_query_handler(lambda c: c.data == 'change_en')
    async def handle_button_click(callback_query: types.CallbackQuery):
        # Extract the message and chat IDs
        message = callback_query.message
        await message.delete()
        chat_id = message.chat.id

        # Send a response message
        set_settings(chat_id, 'en', str(get_mafia_by_chat_id(chat_id)))
        await message.answer(text=get_language(chat_id)['lang_changed'])