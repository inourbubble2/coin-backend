import uuid
import enum

from sqlalchemy import Column, String, DateTime, Float, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

from database.base import Base


class Review(Base):
    __tablename__ = 'reviews'

    writer_id = Column(String, ForeignKey('users.id'), primary_key=True)
    writer = relationship("User", backref="review")

    cafe_id = Column(String, ForeignKey('cafes.id'), primary_key=True)
    cafe = relationship("Cafe", backref="review")

    content = Column(String(200))
    star = Column(Integer())

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))