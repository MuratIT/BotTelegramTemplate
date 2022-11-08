from pydantic import BaseModel


class Admin(BaseModel):
    class Config:
        orm_mode = True


class AdminCreate(Admin):
    id_telegram: int


class AdminUpdate(Admin):
    active: bool


class AdminRead(Admin):
    id: int
    id_telegram: int
    active: bool
