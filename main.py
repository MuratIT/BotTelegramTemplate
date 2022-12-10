import asyncio
import logging
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import Config
from classes.Loading import LoadingModule, LoadingFilters


class TelegramBot:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        self.config = Config().dict()
        self.LoadingModule = LoadingModule()
        self.LoadingFilters = LoadingFilters()

        self.loop = asyncio.get_event_loop()

        self.bot = Bot(token=self.config.get('TOKEN'))
        self.dp = Dispatcher(bot=self.bot, storage=MemoryStorage())

    async def on_startup(self, dp: Dispatcher):
        self.LoadingFilters.load_filters(dp)
        self.LoadingModule.load_modules(dp)

    def run(self):
        executor.start_polling(self.dp, loop=self.loop, skip_updates=True, on_startup=self.on_startup)


if __name__ == "__main__":
    TelegramBot().run()
