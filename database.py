"""
Database setup for the StreamTracker API.

This module configures the SQLAlchemy engine and session for a SQLite
 database stored in movies.db. It also exposes a Base class that
 declarative models should inherit from.
"""
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Use a more user-friendly database location
# If running as executable, use Documents folder, otherwise use current directory
if getattr(sys, 'frozen', False):
    # Running as executable
    documents_path = os.path.join(os.path.expanduser("~"), "Documents", "StreamTracker")
    os.makedirs(documents_path, exist_ok=True)
    db_path = os.path.join(documents_path, "movies.db")
else:
    # Running as script
    db_path = "./movies.db"

SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
