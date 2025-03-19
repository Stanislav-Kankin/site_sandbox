from sqlalchemy import Column, Integer, String, Boolean
from .base import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    importance = Column(Integer, index=True)
    is_done = Column(Boolean, default=False)
