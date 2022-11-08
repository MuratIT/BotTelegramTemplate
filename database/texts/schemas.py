from pydantic import BaseModel


class Text(BaseModel):
    class Config:
        orm_mode = True


class TextCreate(Text):
    text_default: str
    type: str


class TextUpdate(Text):
    text_default: str
    type: str


class TextRead(Text):
    id: int
    text_default: str
    type: str
