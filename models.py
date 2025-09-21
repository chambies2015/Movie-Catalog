"""
SQLAlchemy models for the Movie Tracker API.
Defines the Movie ORM model used to persist movie information.
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String, index=True)
    year = Column(Integer)
    rating = Column(Float)
    watched = Column(Boolean, default=False)
