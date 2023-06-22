from aiogram import Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state import State, RegistrationState, UserInfo
from aiogram.utils.deep_linking import get_start_link



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
        print(registration_state)
        if len(registration_state.users.keys()) >= 2:
            await message.reply("*Игра начинается!*", reply_markup=inline)
        else:
            await message.reply("*Недостаточно игроков*", reply_markup=inline)
