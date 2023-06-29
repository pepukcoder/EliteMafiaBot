from aiogram import types
from aiogram.dispatcher.filters import Filter


class IsGroup(Filter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.SUPERGROUP

class IsPrivate(Filter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE

