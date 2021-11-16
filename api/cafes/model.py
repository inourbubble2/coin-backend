# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

import uuid
import enum

from sqlalchemy import Column, String, DateTime, Float, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

from database.base import Base


# class User(Base):
#     __tablename__ = 'users'
#     id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
#     nickname = Column(String(120), nullable=False)
#     email = Column(String(120), nullable=True)
#     student_year = Column(Integer, nullable=True)
#     dept_code = Column(String(3), nullable=True)


class LocationEnum(enum.Enum):
    front = '정문'
    back = '후문'
    side = '쪽문'


class Cafe(Base):
    __tablename__ = 'cafes'
    id = Column(String(), primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    address = Column(String(), nullable=True)
    open_hour = Column(String(), nullable=True)
    contact = Column(String(), nullable=True)
    link = Column(String(), nullable=True)

    location = Column(Enum(LocationEnum), nullable=True)
    star = Column(Integer(), nullable=True)

    kakao_id = Column(String(), nullable=False)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)

    created_by = Column(String())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))
