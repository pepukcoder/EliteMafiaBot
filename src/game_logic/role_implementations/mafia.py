from aiogram import Bot, types

from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import InteractionTypes

class Mafia(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "🤵🏻Мафия"

    def get_type(self) -> int:
        return Roles.MAFIA.value

    async def send_interactive_messages(self, chat_id: int, bot: Bot):
        state = State()
        game = state.games[chat_id]
        
        user_id = 0
        for usr in game.users:
            if usr.role.get_type() == 1:
                user_id = usr.user_id

        inline_markup = types.InlineKeyboardMarkup(row_width=1)

        for user_state in game.users:
            inline_markup.add(types.InlineKeyboardButton(text=user_state.first_name, callback_data=f"{InteractionTypes.vote_kill}_{user_state.user_id}"))

        await bot.send_message(chat_id=user_id, text="Выбери за кого сегодня будешь голосовать:", reply_markup=inline_markup)