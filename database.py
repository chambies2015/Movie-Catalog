"""
Database setup for the Movie Tracker API.

This module configures the SQLAlchemy engine and session for a SQLite
 database stored in movies.db. It also exposes a Base class that
 declarative models should inherit from.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
