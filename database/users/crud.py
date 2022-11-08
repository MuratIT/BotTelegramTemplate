from sqlalchemy import func

from sqlalchemy import select

from database.base import async_session_maker
from database.crud import Crud

from .users import Users
from .schemas import UserCreate, UserUpdate


class UserCrud(Crud):
    def __init__(self):
        super(UserCrud, self).__init__(Users)

    async def read_user(self, id_telegram: int):
        async with async_session_maker() as session:
            select_user = select(self.model).where(self.model.id_telegram == id_telegram)
            result = await session.execute(select_user)
            model = result.scalars().first()
            return model

    async def update_user(self, id_telegram: int, user_model: UserUpdate):
        user = await self.read_user(id_telegram)
        if user:
            user_model.update_datatime = func.now()
            self.data = user_model.dict()
            await self.update(user.id)

    async def create_user(self, user_model: UserCreate):
        user = await self.read_user(user_model.id_telegram)
        if not user:
            self.data = user_model.dict()
            await self.create()

    async def delete_user(self, id_telegram: int):
        user = await self.read_user(id_telegram)
        if user:
            await self.delete(user.id)


user_crud = UserCrud()
