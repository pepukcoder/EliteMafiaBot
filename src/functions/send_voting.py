from aiogram import Dispatcher, types, Bot

from src.state import State, ChatVoteState
from src.functions import count_dublicates
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.misc import TgKeys
bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

async def send_voting(chat_id: int, user_id: int, user_firstname: str):
    state = State()
    game = state.games[chat_id]

    print(game.chat_votes)
    game.chat_votes = ChatVoteState(vote_for=0, vote_against=0)

    print(game.chat_votes)

    inline_markup = InlineKeyboardMarkup(row_width=1)
    inline_markup.add(InlineKeyboardButton(text=f"👍🏻{game.chat_votes.vote_for}",
                                               callback_data=f"votefor_{user_id}"))
    inline_markup.add(InlineKeyboardButton(text=f"👎🏿{game.chat_votes.vote_against}",
                                               callback_data=f"voteagainst_{user_id}"))
    await bot.send_message(chat_id=chat_id, text=f"Ебашим {user_firstname}?", reply_markup=inline_markup)