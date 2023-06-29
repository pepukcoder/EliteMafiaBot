from aiogram import Dispatcher, executor, types, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state import State, RegistrationState, UserInfo
from aiogram.utils.deep_linking import get_start_link
from src.state import GameState
from src.game_logic import start_loop

from src.functions import delete_reg

from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

def register_start_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['game'])
    async def game(message: types.Message):
        state = State()
        chat_id = message.chat.id

        try:
            registration_state = state.registrations[chat_id]
            msg = await message.reply("Где-то в чате уже зарегестрированна игра")
        except:
            msg = await message.reply("Набор в игру начат!")
            link = await get_start_link(str(chat_id) + ", " + str(msg['message_id']), encode=True)
            state.registrations[chat_id] = RegistrationState(msg['message_id'], {})
            join_button = InlineKeyboardButton(text='Присоединиться', url=link)
            inline = InlineKeyboardMarkup().add(join_button)

            print(state.registrations)

            await msg.edit_text("Набор в игру начат!", reply_markup=inline)


    @dp.message_handler(commands=['start_game'])
    async def start_game(message: types.Message):
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
                await delete_reg(chat_id, bot)
        except KeyError:
            print(f"Registration {chat_id} not found")