from sqlalchemy import Column, Integer, DateTime, func, Boolean
from database.base import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    id_telegram = Column(Integer)
    create_datatime = Column(DateTime, default=func.now())
    update_datatime = Column(DateTime)
    active = Column(Boolean, default=True)
