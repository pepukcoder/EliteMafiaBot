from src.state import Role, State
from src.state.enums import InteractionTypes
from aiogram import Bot, types
class InteractiveMessageSender:
    async def send_interactive_messages(self, chat_id: int, bot: Bot, role: Role):
        state = State()
        game = state.games[chat_id]
        
        user_id = 0
        for usr in game.users:
            if usr.role.get_type() == role.get_type():
                user_id = usr.user_id

        inline_markup = types.InlineKeyboardMarkup(row_width=1)

        for user_state in game.users:
            if user_state.role.get_type() == role.get_type():
                pass
            elif user_state.role.get_type() == 4:
                inline_markup.add(types.InlineKeyboardButton(text=user_state.first_name, callback_data=f"{role.get_type()}_{user_state.user_id}_{chat_id}"))
            else:
                inline_markup.add(types.InlineKeyboardButton(text=user_state.first_name, callback_data=f"{role.get_type()}_{user_state.user_id}_{chat_id}"))

        print(f"{role.get_type()}_{user_state.user_id}_{chat_id}")

        await bot.send_message(chat_id=user_id, text="Выбери взаимодействие:", reply_markup=inline_markup)
