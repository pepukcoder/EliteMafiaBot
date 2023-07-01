from aiogram import Dispatcher, executor, types, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state import State, RegistrationState, UserInfo
from aiogram.utils.deep_linking import get_start_link
from src.state import GameState
from src.game_logic import start_loop

from src.functions import delete_reg

from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
from src.settings.main import get_language
def register_start_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['game'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
    async def game(message: types.Message):
        state = State()
        chat_id = message.chat.id

        try:
            registration_state = state.registrations[chat_id]
            msg = await message.reply(get_language(chat_id)["registered_game_warn"])
        except:
            msg = await message.reply(get_language(chat_id)['game'])
            link = await get_start_link(str(chat_id) + ", " + str(msg['message_id']), encode=True)
            state.registrations[chat_id] = RegistrationState(msg['message_id'], {})
            join_button = InlineKeyboardButton(text=get_language(chat_id)['join'], url=link)
            inline = InlineKeyboardMarkup().add(join_button)

            print(state.registrations)

            await msg.edit_text(get_language(chat_id)['game'], reply_markup=inline)
    @dp.message_handler(commands=['game'], chat_type=types.ChatType.PRIVATE)
    async def game(message: types.Message):
        chat_id = message.chat.id
        await message.answer(get_language(chat_id)['game_warn'])

    @dp.message_handler(commands=['start_game'])
    async def start_game(message: types.Message):
        chat_id = message.chat.id

        state = State()
        try:
            registration_state = state.registrations[chat_id]

            first_names = [item.first_name for item in registration_state.users.values()]

            if len(registration_state.users.keys()) >= 1:
                await message.reply(f"*{get_language(chat_id)['game_start']}*", parse_mode='Markdown')
                await start_loop(chat_id)
            else:
                await message.reply(f"{get_language(chat_id)['no_players']}", parse_mode='Markdown')
                await delete_reg(chat_id, bot)
        except KeyError:
            print(f"Registration {chat_id} not found")