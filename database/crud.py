from sqlalchemy import select

from database.base import async_session_maker


class Crud:
    def __init__(self, model: any, data: dict = None):
        self.model = model
        self.data = data

    async def read_all(self):
        async with async_session_maker() as session:
            select_user = select(self.model)
            result = await session.execute(select_user)
            model = result.scalars().all()
            return model

    async def read_id(self, id: int):
        async with async_session_maker() as session:
            select_user = select(self.model).where(self.model.id == id)
            result = await session.execute(select_user)
            model = result.scalars().first()
            return model

    async def create(self):
        async with async_session_maker() as session:
            user = self.model(**self.data)
            session.add(user)
            await session.commit()

    async def update(self, id: int):
        async with async_session_maker() as session:
            model = await self.read_id(id)
            for key, value in self.data.items():
                setattr(model, key, value)
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model

    async def delete(self, id: int):
        model = await self.read_id(id)
        if model:
            async with async_session_maker() as session:
                await session.delete(model)
                await session.commit()



