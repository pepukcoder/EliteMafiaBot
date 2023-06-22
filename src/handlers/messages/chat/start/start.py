from aiogram import Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state import State, RegistrationState, UserInfo

join_button = InlineKeyboardButton(text='Присоединиться', callback_data="join_handler")
inline = InlineKeyboardMarkup().add(join_button)


def register_start_handlers(dp: Dispatcher):
    state = State()

    @dp.message_handler(commands=['game'])
    async def start_game(message: types.Message):
        chat_id = message.chat.id
        state.registrations.append(RegistrationState(chat_id, {}))

        msg = await message.reply("Набор в игру начат!", reply_markup=inline)

    @dp.callback_query_handler(text=["join_handler"])
    async def game_join(call: types.CallbackQuery):
        if call.data == 'join_handler':
            message = call.message
            chat_id = call.message.chat.id
            user_id = call.from_user.id
            username = call.from_user.username
            first_name = call.from_user.first_name
            registration_state = list(filter(lambda x: x.chat_id == chat_id, state.registrations))[0]
            if not registration_state:
                await call.answer("Problem")

            registration_state.users[user_id] = UserInfo(first_name, username)

            first_names = [item.first_name for item in registration_state.users.values()]
            usernames = [item.username for item in registration_state.users.values()]

            formatted_list = [f"[{name}](t.me/{username})" for name, username in zip(first_names, usernames)]
            print(registration_state)
            try:
                await message.edit_text(
                    "Набор в игру начат!\n*Всего игроков: " + str(len(registration_state.users.keys())) + '*\n' +
                    ', '.join(formatted_list), reply_markup=inline, parse_mode='Markdown',
                    disable_web_page_preview=True)
            except:
                await call.answer("Да ты уже в игре, долбоёб!")

    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        registration_state = list(filter(lambda x: x.chat_id == message.chat.id, state.registrations))[0]
        print(registration_state)
        if len(registration_state.users.keys()) >= 2:
            await message.reply("*Игра начинается!*")
        else:
            await message.reply("*Недостаточно игроков*")
