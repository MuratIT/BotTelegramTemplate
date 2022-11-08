from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from database.admin import admin_crud


class AdminChat(BoundFilter):
    key = 'chat_admin'

    def __init__(self, chat_admin):
        self.chat_admin = chat_admin

    async def check(self, message: any):
        if self.chat_admin:
            if isinstance(message, types.Message) or isinstance(message, types.CallbackQuery):
                if len(await admin_crud.read_all()) == 0:
                    await admin_crud.create_admin(message.from_user.id)
                    return True
                elif await admin_crud.read_admin(message.from_user.id):
                    return True
                return False
        return False
