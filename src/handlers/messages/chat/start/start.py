from aiogram import Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

join_button = InlineKeyboardButton(text='Присоединиться', callback_data="join_handler")
inline = InlineKeyboardMarkup().add(join_button)

connected_users = set()
connected_users_id = set()

def register_start_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['game'])
    async def start_game(message: types.Message):
        msg = await message.reply("Набор в игру начат!", reply_markup=inline)
        @dp.callback_query_handler(text=["join_handler"])
        async def game_join(call: types.CallbackQuery):
                if call.data == 'join_handler':
                    connected_users.add(call.from_user['first_name'])
                    connected_users_id.add(call.from_user['username'])
                    print(connected_users_id)
                    try:
                        await msg.edit_text("Набор в игру начат!\n*Всего игроков: " + str(len(connected_users)) + '*\n' + '_' +
                        ', '.join(connected_users) + '_', reply_markup=inline, parse_mode= 'Markdown')
                    except:
                        await call.answer("Да ты уже в игре, долбоёб!")
                    await call.answer()

    pass