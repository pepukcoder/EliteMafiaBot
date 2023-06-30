from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.misc import TgKeys
from src.handlers import register_all_handlers
import asyncio



async def __on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)

PROXY_URL = "http://proxy.server:3128"
def start_bot():
    setattr(asyncio.sslproto._SSLProtocolTransport, "_start_tls_compatible", True)
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML',proxy="http://proxy.server:3128")
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)