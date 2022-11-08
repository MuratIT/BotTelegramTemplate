from asyncio import get_event_loop, set_event_loop
from aiogram.dispatcher import Dispatcher


class Modules:
    def __init__(self, dp: Dispatcher, loop: get_event_loop or set_event_loop):
        self.dp = dp
        self.loop = loop

    def register_handlers(self):
        pass
