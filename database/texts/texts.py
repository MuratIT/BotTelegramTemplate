from sqlalchemy import Column, Integer, Text, String
from database.base import Base


class Texts(Base):
    __tablename__ = "texts"
    id = Column(Integer, primary_key=True)
    text_default = Column(Text)
    type = Column(String)
