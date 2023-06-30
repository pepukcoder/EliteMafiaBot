from aiogram import Dispatcher, types, Bot

from src.state import State, ChatVoteState
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.misc import TgKeys
bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

def get_name_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.first_name

async def send_voting(chat_id: int, user_id: int):
    state = State()
    chat_votes = ChatVoteState(voting=[])
    game = state.games[chat_id]
    game.chat_votes = chat_votes
    true_count, false_count = game.count_votes()

    if user_id != 0:
        inline_markup = InlineKeyboardMarkup(row_width=1)
        inline_markup.add(InlineKeyboardButton(text=f"👍🏻{true_count}",
                                               callback_data=f"votefor_{user_id}_{chat_id}"))
        inline_markup.add(InlineKeyboardButton(text=f"👎🏿{false_count}",
                                               callback_data=f"voteagainst_{user_id}_{chat_id}"))
    else:
        await bot.send_message(chat_id=chat_id,
                               text="Так как жители - долбоёбы, которые не могут линчевать, мы вынуждены СУКА никого не ЕБАШИТЬ")
    await bot.send_message(chat_id=chat_id, text=f"Ебашим {get_name_by_user_id(chat_id, user_id)}?", reply_markup=inline_markup)