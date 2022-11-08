import logging

from aiogram import types
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, UserDeactivated, TelegramAPIError

from classes.Modules import Modules

from database.users import user_crud, UserUpdate


class Errors(Modules):
    def __init__(self, dp, loop):
        super(Errors, self).__init__(dp, loop)
        self.logging = logging.getLogger('modules.Error')

    async def error_BotBlocked(self, update: types.Update, exception: BotBlocked):
        await user_crud.update_user(update.message.from_user.id, UserUpdate(active=False))
        self.logging.error(f"{exception}")
        return True

    async def error_ChatNotFound(self, update: types.Update, exception: ChatNotFound):
        await user_crud.delete_user(update.message.from_user.id)
        self.logging.error(f"{exception}")
        return True

    async def error_UserDeactivated(self, update: types.Update, exception: UserDeactivated):
        await user_crud.delete_user(update.message.from_user.id)
        self.logging.error(f"{exception}")
        return True

    async def error_TelegramAPIError(self, update: types.Update, exception: TelegramAPIError):
        self.logging.error(f"{exception} - TelegramAPIError - {update}")
        return True

    def register_handlers(self):
        self.dp.register_errors_handler(self.error_BotBlocked, exception=BotBlocked)
        self.dp.register_errors_handler(self.error_ChatNotFound, exception=ChatNotFound)
        self.dp.register_errors_handler(self.error_UserDeactivated, exception=UserDeactivated)
        self.dp.register_errors_handler(self.error_TelegramAPIError, exception=TelegramAPIError)
