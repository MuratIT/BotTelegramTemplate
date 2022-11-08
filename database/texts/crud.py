from sqlalchemy import select

from database.base import async_session_maker
from database.crud import Crud
from .texts import Texts
from .schemas import TextCreate


class TextsCrud(Crud):
    def __init__(self):
        super(TextsCrud, self).__init__(Texts)

    async def read_text(self, types: str):
        async with async_session_maker() as session:
            select_text = select(self.model).where(self.model.type == types)
            result = await session.execute(select_text)
            text_model = result.scalars().first()
            if text_model:
                return text_model
            return Texts()

    async def create_text(self, text_model: TextCreate):
        text = await self.read_text(text_model.type)
        if not text:
            self.data = text_model.dict()
            await self.create()

    async def delete_admin(self, types: str):
        text = await self.read_text(types)
        if text:
            await self.delete(text.id)


texts_crud = TextsCrud()
