from aiogram import Bot, types

from src.state import Role
from src.state.enums import Roles
from src.state import State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.state.enums import InteractionTypes

class Whore(Role):
    async def send_role_name(self, bot: Bot):
        pass

    def __str__(self) -> str:
        return "💃🏼Шлюха"

    def get_type(self) -> int:
        return Roles.WHORE.value

    async def send_interactive_messages(self, chat_id: int, bot: Bot):
        state = State()
        game = state.games[chat_id]
        
        user_id = 0
        for usr in game.users:
            if usr.role.get_type() == 6:
                user_id = usr.user_id

        inline_markup = types.InlineKeyboardMarkup(row_width=1)

        for user_state in game.users:
            inline_markup.add(types.InlineKeyboardButton(text=user_state.first_name, callback_data=f"{InteractionTypes.fuck}_{user_state.user_id}"))

        await bot.send_message(chat_id=user.user_id, text="Выбери кого будешь сегодня клеить:", reply_markup=inline_markup)
