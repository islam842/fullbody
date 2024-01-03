from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config
# Создайте объект MemoryStorage
storage = MemoryStorage()





TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

ADMINS = (1074399140, )
KURATORS = (1074399140, )
