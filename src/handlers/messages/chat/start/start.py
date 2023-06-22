from aiogram import Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state import State, RegistrationState
from src.state.enums import Roles

join_button = InlineKeyboardButton(text='Присоединиться', callback_data="join_handler")
inline = InlineKeyboardMarkup().add(join_button)


def register_start_handlers(dp: Dispatcher):
    state = State()
    @dp.message_handler(commands=['game'])
    async def start_game(message: types.Message):
        chat_id = message.chat.id
        state.registrations.append(RegistrationState(chat_id, set(), set()))

        msg = await message.reply("Набор в игру начат!", reply_markup=inline)

    @dp.callback_query_handler(text=["join_handler"])
    async def game_join(call: types.CallbackQuery):
        if call.data == 'join_handler':
            message = call.message
            chat_id = call.message.chat.id
            user_id = call.from_user.id
            username = call.from_user.username
            registration_state = list(filter(lambda x: x.chat_id == chat_id, state.registrations))[0]
            if not registration_state:
                await call.answer("Problem")

            registration_state.user_ids.add(user_id)
            registration_state.usernames.add(username)
            print(registration_state)
            try:
                await message.edit_text("Набор в игру начат!\n*Всего игроков: " + str(len(registration_state.user_ids)) + '*\n' + '_' +
                                    ', '.join(registration_state.usernames) + '_', reply_markup=inline, parse_mode='Markdown')
            except:
                await call.answer("Да ты уже в игре, долбоёб!")

    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        registration_state = list(filter(lambda x: x.chat_id == message.chat.id, state.registrations))[0]
        print(registration_state)
        if len(registration_state.user_ids) >= 4:
            await message.reply("*Игра начинается!*")
        else:
            await message.reply("*Недостаточно игроков*")




