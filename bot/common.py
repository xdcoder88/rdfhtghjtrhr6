from aiogram import Bot, Dispatcher
from bot.config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
