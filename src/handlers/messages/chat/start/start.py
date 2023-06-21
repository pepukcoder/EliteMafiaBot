from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

join_button = InlineKeyboardButton(text='Присоединиться', callback_data="join_handler")

inline = InlineKeyboardMarkup().add(join_button)

def register_start_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['game'])
    async def start_game(message: types.Message):
        await message.reply("Набор в игру начан! \n Присоединившиеся игроки:", reply_markup=inline)
    @dp.callback_query_handler(text=["join_handler"])
    async def game_join(call: types.CallbackQuery):
        if call.data == 'join_handler':
            await call.message.answer('@Umlaut')

    pass