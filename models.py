"""
SQLAlchemy models for the StreamTracker API.
Defines the Movie and TV Show ORM models used to persist entertainment information.
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String, index=True)
    year = Column(Integer)
    rating = Column(Float, nullable=True)
    watched = Column(Boolean, default=False)
    review = Column(String, nullable=True)
    poster_url = Column(String, nullable=True)


class TVShow(Base):
    __tablename__ = "tv_shows"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    seasons = Column(Integer, nullable=True)
    episodes = Column(Integer, nullable=True)
    rating = Column(Float, nullable=True)
    watched = Column(Boolean, default=False)
    review = Column(String, nullable=True)
    poster_url = Column(String, nullable=True)
