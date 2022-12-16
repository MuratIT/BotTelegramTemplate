import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .Loading import LoadingModule, LoadingFilters
from config import Config


class TelegramBot:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        self.config = Config()
        self.LoadingModule = LoadingModule()
        self.LoadingFilters = LoadingFilters()

        self.bot = Bot(token=self.config.TOKEN)
        self.dp = Dispatcher(bot=self.bot, storage=MemoryStorage())

    async def on_startup(self, dp: Dispatcher):
        self.LoadingFilters.load_filters(dp)
        self.LoadingModule.load_modules(dp)
