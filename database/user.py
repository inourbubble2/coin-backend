import uuid
import enum

from sqlalchemy import Column, String, DateTime, Float, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

from database.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    kakao_id = Column(String(), nullable=False)
    nickname = Column(String(), nullable=False)
    student_type = Column(String())
    student_year = Column(String())

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))
