"""
CRUD utility functions for the Movie Tracker API.
Encapsulates database operations for fetching, creating, updating,
and deleting movie entries.
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
import models
import schemas


def get_movies(
    db: Session,
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    order: Optional[str] = None,
) -> List[models.Movie]:
    query = db.query(models.Movie)
    if search:
        like_pattern = f"%{search}%"
        query = query.filter(
            models.Movie.title.ilike(like_pattern) |
            models.Movie.director.ilike(like_pattern)
        )
    sort_order = asc  # default
    if order and order.lower() == "desc":
        sort_order = desc
    if sort_by == "rating":
        query = query.order_by(sort_order(models.Movie.rating))
    elif sort_by == "year":
        query = query.order_by(sort_order(models.Movie.year))
    return query.all()


def get_movie_by_id(db: Session, movie_id: int) -> Optional[models.Movie]:
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


def create_movie(db: Session, movie: schemas.MovieCreate) -> models.Movie:
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_movie(db: Session, movie_id: int, movie_update: schemas.MovieUpdate) -> Optional[models.Movie]:
    db_movie = get_movie_by_id(db, movie_id)
    if db_movie is None:
        return None
    for field, value in movie_update.dict(exclude_unset=True).items():
        setattr(db_movie, field, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int) -> Optional[models.Movie]:
    db_movie = get_movie_by_id(db, movie_id)
    if db_movie is None:
        return None
    db.delete(db_movie)
    db.commit()
    return db_movie
