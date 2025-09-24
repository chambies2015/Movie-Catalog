"""
CRUD utility functions for the StreamTracker API.
Encapsulates database operations for fetching, creating, updating,
and deleting movie and TV show entries.
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


# TV Show CRUD operations
def get_tv_shows(
    db: Session,
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    order: Optional[str] = None,
) -> List[models.TVShow]:
    query = db.query(models.TVShow)
    if search:
        like_pattern = f"%{search}%"
        query = query.filter(
            models.TVShow.title.ilike(like_pattern)
        )
    sort_order = asc  # default
    if order and order.lower() == "desc":
        sort_order = desc
    if sort_by == "rating":
        query = query.order_by(sort_order(models.TVShow.rating))
    elif sort_by == "year":
        query = query.order_by(sort_order(models.TVShow.year))
    return query.all()


def get_tv_show_by_id(db: Session, tv_show_id: int) -> Optional[models.TVShow]:
    return db.query(models.TVShow).filter(models.TVShow.id == tv_show_id).first()


def create_tv_show(db: Session, tv_show: schemas.TVShowCreate) -> models.TVShow:
    db_tv_show = models.TVShow(**tv_show.dict())
    db.add(db_tv_show)
    db.commit()
    db.refresh(db_tv_show)
    return db_tv_show


def update_tv_show(db: Session, tv_show_id: int, tv_show_update: schemas.TVShowUpdate) -> Optional[models.TVShow]:
    db_tv_show = get_tv_show_by_id(db, tv_show_id)
    if db_tv_show is None:
        return None
    for field, value in tv_show_update.dict(exclude_unset=True).items():
        setattr(db_tv_show, field, value)
    db.commit()
    db.refresh(db_tv_show)
    return db_tv_show


def delete_tv_show(db: Session, tv_show_id: int) -> Optional[models.TVShow]:
    db_tv_show = get_tv_show_by_id(db, tv_show_id)
    if db_tv_show is None:
        return None
    db.delete(db_tv_show)
    db.commit()
    return db_tv_show


# Export/Import functions
def get_all_movies(db: Session) -> List[models.Movie]:
    """Get all movies for export"""
    return db.query(models.Movie).all()


def get_all_tv_shows(db: Session) -> List[models.TVShow]:
    """Get all TV shows for export"""
    return db.query(models.TVShow).all()


def find_movie_by_title_and_director(db: Session, title: str, director: str) -> Optional[models.Movie]:
    """Find a movie by title and director for import conflict resolution"""
    return db.query(models.Movie).filter(
        models.Movie.title == title,
        models.Movie.director == director
    ).first()


def find_tv_show_by_title_and_year(db: Session, title: str, year: int) -> Optional[models.TVShow]:
    """Find a TV show by title and year for import conflict resolution"""
    return db.query(models.TVShow).filter(
        models.TVShow.title == title,
        models.TVShow.year == year
    ).first()


def import_movies(db: Session, movies: List[schemas.MovieCreate]) -> tuple[int, int, List[str]]:
    """Import movies, returning (created_count, updated_count, errors)"""
    created = 0
    updated = 0
    errors = []
    
    for movie_data in movies:
        try:
            # Check if movie already exists
            existing_movie = find_movie_by_title_and_director(
                db, movie_data.title, movie_data.director
            )
            
            if existing_movie:
                # Update existing movie
                for field, value in movie_data.dict(exclude_unset=True).items():
                    setattr(existing_movie, field, value)
                updated += 1
            else:
                # Create new movie
                db_movie = models.Movie(**movie_data.dict())
                db.add(db_movie)
                created += 1
        except Exception as e:
            errors.append(f"Error importing movie '{movie_data.title}': {str(e)}")
    
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        errors.append(f"Database error during movie import: {str(e)}")
        return 0, 0, errors
    
    return created, updated, errors


def import_tv_shows(db: Session, tv_shows: List[schemas.TVShowCreate]) -> tuple[int, int, List[str]]:
    """Import TV shows, returning (created_count, updated_count, errors)"""
    created = 0
    updated = 0
    errors = []
    
    for tv_show_data in tv_shows:
        try:
            # Check if TV show already exists
            existing_tv_show = find_tv_show_by_title_and_year(
                db, tv_show_data.title, tv_show_data.year
            )
            
            if existing_tv_show:
                # Update existing TV show
                for field, value in tv_show_data.dict(exclude_unset=True).items():
                    setattr(existing_tv_show, field, value)
                updated += 1
            else:
                # Create new TV show
                db_tv_show = models.TVShow(**tv_show_data.dict())
                db.add(db_tv_show)
                created += 1
        except Exception as e:
            errors.append(f"Error importing TV show '{tv_show_data.title}': {str(e)}")
    
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        errors.append(f"Database error during TV show import: {str(e)}")
        return 0, 0, errors
    
    return created, updated, errors