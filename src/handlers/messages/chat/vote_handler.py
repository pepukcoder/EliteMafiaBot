from aiogram import Dispatcher, types, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.state import State, VoteState, ChatVoteState
from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_chat_vote_handler(dp: Dispatcher):
    @dp.callback_query_handler(regexp="votefor_(\d+)_(\-?\d+)")
    async def vote_handler(call: types.CallbackQuery):
        state = State()
        text_vote, object_id, chat_id = call.data.split("_")
        game = state.games[int(chat_id)]
        user_id = int(call.from_user.id)

        # remove oposite vote
        game.remove_opposite_vote(user_id)

        # Check if the user has already voted
        if game.chat_votes.voting and any(user_id == vote[0] for vote in game.chat_votes.voting):
            # Check if the user has already voted
            existing_vote = next((vote for vote in game.chat_votes.voting if vote[0] == user_id), None)
            if existing_vote[1] is False:
                existing_vote[1] = True  # Change the existing vote to True
                await call.answer("Ваш голос изменен на 👍", show_alert=True)
                return

            await call.answer("Вы уже проголосовали", show_alert=True)
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
        await call.answer("Вы проголосовали 👍")
        await call.message.edit_text(text=f"Ебашим {object_id}?", reply_markup=inline_markup)

    @dp.callback_query_handler(regexp="voteagainst_(\d+)_(\-?\d+)")
    async def vote_handler(call: types.CallbackQuery):
        state = State()
        text_vote, object_id, chat_id = call.data.split("_")
        game = state.games[int(chat_id)]
        user_id = int(call.from_user.id)

        # remove oposite vote
        game.remove_opposite_vote(user_id)

        # Check if the user has already voted
        if game.chat_votes.voting and any(user_id == vote[0] for vote in game.chat_votes.voting):
            # Check if the user has already voted
            existing_vote = next((vote for vote in game.chat_votes.voting if vote[0] == user_id), None)
            if existing_vote[1] is True:
                existing_vote[1] = False  # Change the existing vote to True
                await call.answer("Ваш голос изменен на 👎", show_alert=True)
                return

            await call.answer("Вы уже проголосовали", show_alert=True)
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
        await call.answer("Вы проголосовали 👎")
        await call.message.edit_text(text=f"Ебашим {object_id}?", reply_markup=inline_markup)