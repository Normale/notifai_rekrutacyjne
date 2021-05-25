from sqlalchemy import String, Column, Integer
from database import Base


class Message(Base):
    __tablename__ = "messages"

    text = Column(String(length=160))
    views = Column(Integer, default=0)
    nr = Column(Integer, primary_key=True, index=True)
