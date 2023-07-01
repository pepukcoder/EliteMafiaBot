from aiogram import Dispatcher, types, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.state import State, VoteState, ChatVoteState
from src.misc import TgKeys
from src.settings.main import get_language

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def get_name_by_user_id(chat_id: int, user_id: int):
    state = State()
    game = state.games[chat_id]

    for user in game.users:
        if user.user_id == user_id:
            return user.first_name

def register_chat_vote_handler(dp: Dispatcher):
    @dp.callback_query_handler(regexp="votefor_(\d+)_(\-?\d+)")
    async def vote_handler(call: types.CallbackQuery):
        state = State()
        text_vote, object_id, chat_id = call.data.split("_")
        print(object_id)
        game = state.games[int(chat_id)]
        user_id = call.from_user.id
        game.chat_votes.vote_for = int(object_id)
        game.chat_votes.message_id = call.message.message_id
        # remove oposite vote
        game.decrease_false_count(user_id)

        print(user_id, int(object_id))

        # check if user is alive
        users = state.games[int(chat_id)].users
        for user in users:
            if user_id == user.user_id:
                break
            if user_id == int(object_id):
                print('f')
                await call.answer(f"{get_language(chat_id)['vote_isyou']}")
                return
        else:
            await call.answer(f"{get_language(chat_id)['vote_notplayer']}", show_alert=True)
            return


        # Check if the user has already voted
        if game.chat_votes.voting and any(user_id == vote[0] for vote in game.chat_votes.voting):
            # Check if the user has already voted
            existing_vote = next((vote for vote in game.chat_votes.voting if vote[0] == user_id), None)
            if existing_vote[1] is False:
                existing_vote[1] = True  # Change the existing vote to True
                await call.answer(f"{get_language(chat_id)['vote_change_true']}", show_alert=True)
                return

            await call.answer(f"{get_language(chat_id)['vote_already']}", show_alert=True)
            return

        # Increase the true count for the user
        game.increase_true_count(user_id)
        true_count, false_count = game.count_votes()

        inline_markup = InlineKeyboardMarkup(row_width=1)
        inline_markup.add(InlineKeyboardButton(text=f"👍🏻{true_count}",
                                               callback_data=f"votefor_{object_id}_{chat_id}"))
        inline_markup.add(InlineKeyboardButton(text=f"👎🏿{false_count}",
                                               callback_data=f"voteagainst_{object_id}_{chat_id}"))

        print(game.chat_votes)
        await call.answer(f"{get_language(chat_id)['vote_true']}")
        await call.message.edit_reply_markup(reply_markup=inline_markup)

    @dp.callback_query_handler(regexp="voteagainst_(\d+)_(\-?\d+)")
    async def vote_handler(call: types.CallbackQuery):
        state = State()
        text_vote, object_id, chat_id = call.data.split("_")
        game = state.games[int(chat_id)]
        print(object_id)
        user_id = call.from_user.id
        game.chat_votes.vote_for = int(object_id)
        game.chat_votes.message_id = call.message.message_id
        # remove oposite vote
        game.decrease_true_count(user_id)

        print(user_id, int(object_id))

        #check if user is alive
        users = state.games[int(chat_id)].users
        for user in users:
            if user_id == user.user_id:
                break

            if user_id == int(object_id):
                print('f')
                await call.answer(f"{get_language(chat_id)['vote_isyou']}")
                return
        else:
            await call.answer(f"{get_language(chat_id)['vote_notplayer']}", show_alert=True)
            return

        # Check if the user has already voted
        if game.chat_votes.voting and any(user_id == vote[0] for vote in game.chat_votes.voting):
            # Check if the user has already voted
            existing_vote = next((vote for vote in game.chat_votes.voting if vote[0] == user_id), None)
            if existing_vote[1] is True:
                existing_vote[1] = False  # Change the existing vote to True
                await call.answer(f"{get_language(chat_id)['vote_change_false']}", show_alert=True)
                return

            await call.answer(f"{get_language(chat_id)['vote_already']}", show_alert=True)
            return

        # Increase the false count for the user
        game.increase_false_count(user_id)
        true_count, false_count = game.count_votes()

        inline_markup = InlineKeyboardMarkup(row_width=1)
        inline_markup.add(InlineKeyboardButton(text=f"👍🏻{true_count}",
                                               callback_data=f"votefor_{object_id}_{chat_id}"))
        inline_markup.add(InlineKeyboardButton(text=f"👎🏿{false_count}",
                                               callback_data=f"voteagainst_{object_id}_{chat_id}"))

        print(game.chat_votes)
        await call.answer(f"{get_language(chat_id)['vote_false']}")
        await call.message.edit_reply_markup(reply_markup=inline_markup)