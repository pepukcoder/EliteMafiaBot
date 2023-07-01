from aiogram import Dispatcher, Bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.deep_linking import decode_payload

from src.misc import TgKeys
from src.settings import get_language
from src.state import State, UserInfo

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_start_handler(dp: Dispatcher):

    @dp.message_handler(commands=["start"])
    async def handler(message: Message):
        args = message.get_args()
        payload = decode_payload(args)


        if payload:
            chat_id = int(payload.split(',', 1)[0])
            print(args)
            join_button = InlineKeyboardButton(text=get_language(chat_id)['join'],
                                               url="https://t.me/elite_mafia_bot?start=" + args)
            inline = InlineKeyboardMarkup().add(join_button)
            message_id = int(payload.split(',', 1)[-1].replace(" ", ""))
            user_id = message.from_user.id
            first_name = message.from_user.first_name
            link = f'[{first_name}](tg://user?id={user_id})'
            print(message_id, chat_id, user_id, first_name, link)

            state = State()

            try:
                registration_state = state.registrations[chat_id]

                if not registration_state:
                    await message.answer("Problem")

                registration_state.users[user_id] = UserInfo(first_name, link)

                links = [item.link for item in registration_state.users.values()]
                # usernames = [item.username for item in registration_state.users.values()]
                # formatted_list = [f"[{name}](t.me/{username})" for name, username in zip(first_names, usernames)]

                print(registration_state)
                try:
                    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                text=(f"{get_language(chat_id)['game']}\n*{get_language(chat_id)['all']} " + str(
                                                    len(registration_state.users.keys())) + '*\n' +
                                                      ', '.join(links)), parse_mode='Markdown', reply_markup=inline,
                                                disable_web_page_preview=True)
                    await message.answer(f"{get_language(chat_id)['game_joined']}")
                except:
                    await message.answer(f"{get_language(chat_id)['alr_in_game']}")
            except KeyError:
                print(f"Registration {chat_id} not found")
        else:
            chat_id = message.from_user.id
            await message.answer(f"{get_language(chat_id)['reg_thr_chat']}")
