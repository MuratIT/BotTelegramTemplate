from sqlalchemy import Column, Integer
from database.base import Base


class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True)
    id_telegram = Column(Integer)
