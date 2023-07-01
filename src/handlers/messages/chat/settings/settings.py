from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Dispatcher
from src.settings.main import get_language, set_settings, get_settings


def register_settings_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['settings'])
    async def settings(message: types.Message):
        chat_id = message.chat.id

        try:
            print(get_language(chat_id)['language'])
            msg = await message.reply(get_language(chat_id)['language'])
        except:
            set_settings(chat_id, 'uk')
            msg = await message.reply(get_language(chat_id)['language'])


        lang_1 = InlineKeyboardButton(text="Русский🇷🇺", callback_data="change_ru")
        lang_2 = InlineKeyboardButton(text="Українська🇺🇦", callback_data="change_ua")
        inline = InlineKeyboardMarkup().add(lang_1, lang_2)
        await msg.edit_text(get_language(chat_id)['settings'], reply_markup=inline)

    @dp.callback_query_handler(lambda c: c.data == 'change_ru')
    async def handle_button_click(callback_query: types.CallbackQuery):
        # Extract the message and chat IDs
        message = callback_query.message
        await message.delete()
        chat_id = message.chat.id

        # Send a response message
        set_settings(chat_id, 'ru')
        await message.answer(text=get_language(chat_id)['lang_changed'])

    @dp.callback_query_handler(lambda c: c.data == 'change_ua')
    async def handle_button_click(callback_query: types.CallbackQuery):
        # Extract the message and chat IDs
        message = callback_query.message
        await message.delete()
        chat_id = message.chat.id

        # Send a response message
        set_settings(chat_id, 'uk')
        await message.answer(text=get_language(chat_id)['lang_changed'])
