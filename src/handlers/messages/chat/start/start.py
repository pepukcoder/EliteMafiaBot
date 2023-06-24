from aiogram import Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state import State, RegistrationState, UserInfo
from aiogram.utils.deep_linking import get_start_link
from src.state import GameState
from src.game_logic import start_loop

def register_start_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['game'])
    async def start_game(message: types.Message):
        state = State()
        chat_id = message.chat.id

        state.registrations[chat_id] = RegistrationState({})

        msg = await message.reply("Набор в игру начат!")
        link = await get_start_link(str(chat_id) + ", " + str(msg['message_id']), encode=True)
        join_button = InlineKeyboardButton(text='Присоединиться', url=link)
        inline = InlineKeyboardMarkup().add(join_button)

        await msg.edit_text("Набор в игру начат!", reply_markup=inline)

    @dp.message_handler(commands=['start_game'])
    async def send_welcome(message: types.Message):
        chat_id = message.chat.id

        state = State()
        try:
            registration_state = state.registrations[chat_id]

            first_names = [item.first_name for item in registration_state.users.values()]

            if len(registration_state.users.keys()) >= 1:
                await message.reply("*Игра начинается!*", parse_mode='Markdown')
                await start_loop(chat_id)
            else:
                await message.reply("*Недостаточно игроков*", parse_mode='Markdown')
        except KeyError:
            print(f"Registration {chat_id} not found")
