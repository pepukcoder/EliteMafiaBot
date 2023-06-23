from aiogram import Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state import State, RegistrationState, UserInfo
from aiogram.utils.deep_linking import get_start_link
from src.game_logic.role_implementations import assign

state = State()


def register_start_handlers(dp: Dispatcher):
    state = State()

    @dp.message_handler(commands=['game'])
    async def start_game(message: types.Message):
        chat_id = message.chat.id
        state.registrations.append(RegistrationState(chat_id, {}))

        msg = await message.reply("Набор в игру начат!")
        link = await get_start_link(str(chat_id) + ", " + str(msg['message_id']), encode=True)
        join_button = InlineKeyboardButton(text='Присоединиться', url=link)
        inline = InlineKeyboardMarkup().add(join_button)

        await msg.edit_text("Набор в игру начат!", reply_markup=inline)

    @dp.message_handler(commands=['start_game'])
    async def send_welcome(message: types.Message):
        registration_state = list(filter(lambda x: x.chat_id == message.chat.id, state.registrations))[0]
        #print(list(registration_state.users.keys())[0])

        user_ids = []

        for key in registration_state.users.keys():
            user_ids.append(key)

        print(user_ids)

        if len(registration_state.users.keys()) >= 2:
            await message.reply("*Игра начинается!*", parse_mode='Markdown')
            x = assign(registration_state)
            for user in x:
                role_name = user.role.__class__.__name__ if user.role else "Мирный житель"
                #await message.reply(f"Username: {user.username}, id: {user.user_id}, Role: {role_name}")
                await message.reply(f"Твоя роль - {role_name}")
        else:
            await message.reply("*Недостаточно игроков*", parse_mode='Markdown')
