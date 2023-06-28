from aiogram import Dispatcher, types, Bot

from src.state import State, VoteState
from src.misc import TgKeys

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


def register_vote_handler(dp: Dispatcher):
    @dp.callback_query_handler(regexp="voting_(\d+)_(\-?\d+)")
    async def vote_handler(call: types.CallbackQuery):
        await call.message.delete()

        state = State()
        obj, object_id, chat_id = call.data.split("_")
        vote_subjects = [vote.vote_subject for vote in state.games[int(chat_id)].votes]
        print(vote_subjects)  # output []

        user_id = call.from_user.id

        day = state.games[int(chat_id)].day
        state.games[int(chat_id)].votes.append(VoteState(vote_subject=int(user_id), vote_object=int(object_id)))
        await call.message.answer(text="Вы проголосовали.")
        await bot.send_message(chat_id=int(chat_id), text=f"{call.from_user.first_name} проголосовал.")