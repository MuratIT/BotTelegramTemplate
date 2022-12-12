import logging

from aiogram import types
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, UserDeactivated, TelegramAPIError

from classes.Modules import Modules


class Errors(Modules):
    def __init__(self, dp):
        super(Errors, self).__init__(dp)
        self.logging = logging.getLogger('modules.Error')

    async def error_BotBlocked(self, update: types.Update, exception: BotBlocked):
        self.logging.error(f"{exception} - BotBlocked - {update}")
        return True

    async def error_ChatNotFound(self, update: types.Update, exception: ChatNotFound):
        self.logging.error(f"{exception} - ChatNotFound - {update}")
        return True

    async def error_UserDeactivated(self, update: types.Update, exception: UserDeactivated):
        self.logging.error(f"{exception} - UserDeactivated - {update}")
        return True

    async def error_TelegramAPIError(self, update: types.Update, exception: TelegramAPIError):
        self.logging.error(f"{exception} - TelegramAPIError - {update}")
        return True

    def register_handlers(self):
        self.dp.register_errors_handler(self.error_BotBlocked, exception=BotBlocked)
        self.dp.register_errors_handler(self.error_ChatNotFound, exception=ChatNotFound)
        self.dp.register_errors_handler(self.error_UserDeactivated, exception=UserDeactivated)
        self.dp.register_errors_handler(self.error_TelegramAPIError, exception=TelegramAPIError)
