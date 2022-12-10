from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class PrivateChat(BoundFilter):
    key = 'chat_private'

    def __init__(self, chat_private):
        self.chat_private = chat_private

    async def check(self, message: any):
        if self.chat_private:
            if isinstance(message, types.Message):
                if message.chat.type == 'private':
                    return self.chat_private
                return not self.chat_private
            elif isinstance(message, types.CallbackQuery):
                if message.message.chat.type == 'private':
                    return self.chat_private
                return not self.chat_private
            return not self.chat_private
        return self.chat_private
