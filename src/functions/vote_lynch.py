from aiogram import Dispatcher, types, Bot
from src.state import State, ChatVoteState
from src.functions import Delete

def get_name_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.first_name

async def vote_lynch(chat_id, bot: Bot):
    state = State()
    game = state.games[chat_id]
    try:
        true_count, false_count = game.count_votes()
    except:
        true_count = 0
        false_count = 0
    try:
        user = game.chat_votes.vote_for
        msg_id = game.chat_votes.message_id
        if true_count > false_count:
            await bot.delete_message(chat_id, msg_id)
            await bot.send_message(chat_id, f"*Заебашен {get_name_by_user_id(chat_id, user)}!*\n👍{true_count} | 👎🏿{false_count}",
                                   parse_mode='Markdown')
            Delete.delete_all_elements_by_id(chat_id, [user])
        else:
            await bot.delete_message(chat_id, msg_id)
            await bot.send_message(chat_id,
                                   f"Из-за того, что жители только и делали, что пиздели, они не смогли договориться, кого линчевать.",
                                   parse_mode='Markdown')
    except:
        await bot.send_message(chat_id,
                               f"None ",
                               parse_mode='Markdown')