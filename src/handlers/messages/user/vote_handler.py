from aiogram import Dispatcher, types, Bot

from src.state import State, VoteState
from src.functions import get_role_by_user_id
from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_vote_handler(dp: Dispatcher):
    @dp.callback_query_handler(regexp="voting_(\d+)_(\-?\d+)")
    async def vote_handler(call: types.CallbackQuery):
        await call.message.delete()

        state = State()
        obj, object_id, chat_id = call.data.split("_")
        vote_subjects = [vote.vote_subject for vote in state.games[int(chat_id)].votes]
          # output []

        user_id = call.from_user.id

        day = state.games[int(chat_id)].day
        state.games[int(chat_id)].votes.append(VoteState(vote_subject=int(user_id), vote_object=int(object_id)))
        await call.message.answer(text="Вы проголосовали")
        await bot.send_message(chat_id=int(chat_id), text=f"{call.from_user.first_name} проголосовал")

    @dp.callback_query_handler(regexp="skipvote_(\-?\d+)")
    async def skip_handler(call: types.CallbackQuery):
        await call.message.delete()
        state = State()
        skip_text, chat_id = call.data.split("_")
        user_id = call.from_user.id
        day = state.games[int(chat_id)].day
        state.games[int(chat_id)].votes.append(VoteState(vote_subject=int(user_id), vote_object=0))

        await call.message.answer("Вы пропустили голосование")
        await bot.send_message(chat_id=int(chat_id), text=f"🚷{call.from_user.first_name} сидит дома и молча дрочит")
