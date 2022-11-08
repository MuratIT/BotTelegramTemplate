from sqlalchemy import select

from database.base import async_session_maker
from database.crud import Crud
from .admin import Admin
from .schemas import AdminCreate


class AdminCrud(Crud):
    def __init__(self):
        super(AdminCrud, self).__init__(Admin)

    async def read_admin(self, id_telegram: int):
        async with async_session_maker() as session:
            select_user = select(self.model).where(self.model.id_telegram == id_telegram)
            result = await session.execute(select_user)
            admin_model = result.scalars().first()
            return admin_model

    async def create_admin(self, admin_create: AdminCreate):
        admin = await self.read_admin(admin_create.id_telegram)
        if not admin:
            self.data = admin_create.dict()
            await self.create()

    async def delete_admin(self, id_telegram: int):
        admin = await self.read_admin(id_telegram)
        if admin:
            await self.delete(admin.id)


admin_crud = AdminCrud()
