from aiogram import Dispatcher, types, Bot

from src.state import State, ChatVoteState
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.misc import TgKeys
bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


async def send_voting(chat_id: int, user_id: int, user_firstname: str):
    state = State()
    chat_votes = ChatVoteState(voting=[], vote_for=0, message_id=0)
    game = state.games[chat_id]
    game.chat_votes = chat_votes
    true_count, false_count = game.count_votes()

    inline_markup = InlineKeyboardMarkup(row_width=1)
    inline_markup.add(InlineKeyboardButton(text=f"👍🏻{true_count}",
                                               callback_data=f"votefor_{user_id}_{chat_id}"))
    inline_markup.add(InlineKeyboardButton(text=f"👎🏿{false_count}",
                                               callback_data=f"voteagainst_{user_id}_{chat_id}"))
    await bot.send_message(chat_id=chat_id, text=f"Ебашим {user_firstname}?", reply_markup=inline_markup)