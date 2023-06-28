from aiogram import Dispatcher, types, Bot
from src.state import State, ChatVoteState
from src.functions import Delete
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def vote_lynch(chat_id, bot: Bot):
    state = State()
    game = state.games[chat_id]
    true_count, false_count = game.count_votes()
    user = game.chat_votes.vote_for
    msg_id = game.chat_votes.message_id
    if true_count > false_count:
        await bot.delete_message(chat_id, msg_id)
        await bot.send_message(chat_id, f"*Заебашен {user}!*\n👍{true_count} | 👎🏿{false_count}", parse_mode='Markdown')
        Delete.delete_all_elements_by_id(chat_id, [user])
    else:
        await bot.send_message(chat_id, f"Из-за того, что жители только и делали, что пиздели, они не смогли договориться, кого линчевать.", parse_mode='Markdown')
