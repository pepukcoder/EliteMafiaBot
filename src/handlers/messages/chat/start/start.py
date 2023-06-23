from aiogram import Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state import State, RegistrationState, UserInfo
from aiogram.utils.deep_linking import get_start_link
from src.state import GameState
from src.game_logic import start_loop

state = State()

def register_start_handlers(dp: Dispatcher):

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
        chat_id = message.chat.id

        first_names = [item.first_name for item in registration_state.users.values()]

        if len(registration_state.users.keys()) >= 2:
            await message.reply("*Игра начинается!*", parse_mode='Markdown')
            await start_loop(registration_state, chat_id)
        else:
            await message.reply("*Недостаточно игроков*", parse_mode='Markdown')
