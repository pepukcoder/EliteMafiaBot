from aiogram import Dispatcher, Bot
from aiogram.utils.deep_linking import decode_payload
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from src.state import State, RegistrationState, UserInfo
from aiogram.utils.deep_linking import get_start_link
from src.misc import TgKeys

def register_user_handlers(dp: Dispatcher):
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
    state = State()

    @dp.message_handler(commands=["start"])
    async def handler(message: Message):
        args = message.get_args()
        payload = decode_payload(args)
        print(args)
        join_button = InlineKeyboardButton(text='Присоединиться', url="https://t.me/elite_mafia_bot?start="+args)
        inline = InlineKeyboardMarkup().add(join_button)

        if payload:
            chat_id = int(payload.split(',', 1)[0])
            message_id = int(payload.split(',', 1)[-1].replace(" ", ""))
            user_id = message.from_user.id
            username = message.from_user.username
            first_name = message.from_user.first_name
            print(message_id, chat_id, user_id, username, first_name)

            registration_state = list(filter(lambda x: x.chat_id == chat_id, state.registrations))[0]
            if not registration_state:
                await message.answer("Problem")

            registration_state.users[user_id] = UserInfo(first_name, username)

            first_names = [item.first_name for item in registration_state.users.values()]
            usernames = [item.username for item in registration_state.users.values()]

            formatted_list = [f"[{name}](t.me/{username})" for name, username in zip(first_names, usernames)]
            print(registration_state)
            try:
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                    text=("Набор в игру начат!\n*Всего игроков: " + str(len(registration_state.users.keys())) + '*\n' +
                    ', '.join(formatted_list)), parse_mode='Markdown', reply_markup=inline,
                    disable_web_page_preview=True)
                await message.answer(f"Ты зарегестрировался в игре.")
            except:
                await message.answer('ДА ТЫ УЖЕ В ИГРЕ, ДОЛБОЁБ!')
        else:
            await message.answer(f"Зарегестрируйтесь через чат")
    
    
    
    pass
