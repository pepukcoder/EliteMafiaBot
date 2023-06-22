from aiogram import Bot, Dispatcher, executor, types
from src.state import GameState
from src.state.enums import Roles

def register_game_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        await message.reply("*Игра начинается!*")
        #TODO:
        #load role rules
        #assign roles randomly

    pass
