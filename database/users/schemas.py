from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    class Config:
        orm_mode = True


class UserCreate(User):
    id_telegram: int


class UserUpdate(User):
    update_datatime: Optional[datetime]
    active: bool


class UserRead(User):
    id: int
    id_telegram: int
    create_datatime: Optional[datetime]
    update_datatime: Optional[datetime]
    active: bool
