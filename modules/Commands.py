from aiogram.types import Message

from classes.Modules import Modules

from database.users import user_crud, UserCreate
from database.texts import texts_crud


class Commands(Modules):
    @staticmethod
    async def start(message: Message):
        if message.chat.type == 'private':
            await user_crud.create_user(UserCreate(id_telegram=message.from_user.id))

        text = await texts_crud.read_text('start')
        await message.answer(text.text_default)

    @staticmethod
    async def help(message: Message):
        text = await texts_crud.read_text('help')
        await message.answer(text.text_default)

    def register_handlers(self):
        self.dp.register_message_handler(callback=self.start, commands=['start'], chat_private=True)
        self.dp.register_message_handler(callback=self.help, commands=['help'], chat_private=True)
