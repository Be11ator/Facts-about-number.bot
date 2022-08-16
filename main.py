from aiogram import  types, executor, Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN



bot = Bot(TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot,storage=storage)