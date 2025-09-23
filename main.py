"""
Entry point for the StreamTracker API.
Provides CRUD endpoints for managing movies and TV shows.
"""
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import inspect, text

import crud
import schemas
from database import Base, SessionLocal, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

# Lightweight migration: add missing columns if upgrading an existing DB
try:
    inspector = inspect(engine)
    
    # Check movies table for review and poster_url columns
    existing_columns = {col["name"] for col in inspector.get_columns("movies")}
    if "review" not in existing_columns:
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE movies ADD COLUMN review VARCHAR"))
            conn.commit()
    if "poster_url" not in existing_columns:
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE movies ADD COLUMN poster_url VARCHAR"))
            conn.commit()
    
    # Check tv_shows table for schema migration
    if inspector.has_table("tv_shows"):
        tv_columns = {col["name"] for col in inspector.get_columns("tv_shows")}
        
        # If we have the old schema (creator, year_started, year_ended), migrate to new schema
        if "creator" in tv_columns and "year_started" in tv_columns:
            with engine.connect() as conn:
                # Create a backup table with old data
                conn.execute(text("CREATE TABLE tv_shows_backup AS SELECT * FROM tv_shows"))
                
                # Drop the old table
                conn.execute(text("DROP TABLE tv_shows"))
                
                # Recreate the table with new schema
                conn.execute(text("""
                    CREATE TABLE tv_shows (
                        id INTEGER PRIMARY KEY,
                        title VARCHAR,
                        year INTEGER,
                        seasons INTEGER,
                        episodes INTEGER,
                        rating FLOAT,
                        watched BOOLEAN DEFAULT 0,
                        review VARCHAR,
                        poster_url VARCHAR
                    )
                """))
                
                # Migrate data from backup (use year_started as the year)
                conn.execute(text("""
                    INSERT INTO tv_shows (id, title, year, seasons, episodes, rating, watched, review, poster_url)
                    SELECT id, title, year_started, seasons, episodes, rating, watched, review, NULL
                    FROM tv_shows_backup
                """))
                
                # Drop the backup table
                conn.execute(text("DROP TABLE tv_shows_backup"))
                
                conn.commit()
                print("Successfully migrated tv_shows table to new schema")
        else:
            # If table exists but doesn't have poster_url column, add it
            if "poster_url" not in tv_columns:
                with engine.connect() as conn:
                    conn.execute(text("ALTER TABLE tv_shows ADD COLUMN poster_url VARCHAR"))
                    conn.commit()
    
except Exception as e:
    # Best-effort migration; avoid crashing app startup if inspection fails
    print(f"Migration warning: {e}")
    pass

# Initialize FastAPI
app = FastAPI(title="StreamTracker API", description="Manage your movies and TV shows", version="0.1.0")

# Configure CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "StreamTracker API is running \U0001f680"}


# Movie endpoints
@app.get("/movies/", response_model=List[schemas.Movie], tags=["movies"])
async def list_movies(
        search: Optional[str] = None,
        sort_by: Optional[str] = None,
        order: Optional[str] = None,  # new
        db: Session = Depends(get_db),
):
    return crud.get_movies(db, search=search, sort_by=sort_by, order=order)


@app.get("/movies/{movie_id}", response_model=schemas.Movie, tags=["movies"])
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_id(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@app.post("/movies/", response_model=schemas.Movie, status_code=201, tags=["movies"])
async def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)


@app.put("/movies/{movie_id}", response_model=schemas.Movie, tags=["movies"])
async def update_movie(movie_id: int, movie: schemas.MovieUpdate, db: Session = Depends(get_db)):
    db_movie = crud.update_movie(db, movie_id, movie)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@app.delete("/movies/{movie_id}", response_model=schemas.Movie, tags=["movies"])
async def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.delete_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


# TV Show endpoints
@app.get("/tv-shows/", response_model=List[schemas.TVShow], tags=["tv-shows"])
async def list_tv_shows(
        search: Optional[str] = None,
        sort_by: Optional[str] = None,
        order: Optional[str] = None,
        db: Session = Depends(get_db),
):
    return crud.get_tv_shows(db, search=search, sort_by=sort_by, order=order)


@app.get("/tv-shows/{tv_show_id}", response_model=schemas.TVShow, tags=["tv-shows"])
async def get_tv_show(tv_show_id: int, db: Session = Depends(get_db)):
    db_tv_show = crud.get_tv_show_by_id(db, tv_show_id)
    if db_tv_show is None:
        raise HTTPException(status_code=404, detail="TV Show not found")
    return db_tv_show


@app.post("/tv-shows/", response_model=schemas.TVShow, status_code=201, tags=["tv-shows"])
async def create_tv_show(tv_show: schemas.TVShowCreate, db: Session = Depends(get_db)):
    return crud.create_tv_show(db, tv_show)


@app.put("/tv-shows/{tv_show_id}", response_model=schemas.TVShow, tags=["tv-shows"])
async def update_tv_show(tv_show_id: int, tv_show: schemas.TVShowUpdate, db: Session = Depends(get_db)):
    db_tv_show = crud.update_tv_show(db, tv_show_id, tv_show)
    if db_tv_show is None:
        raise HTTPException(status_code=404, detail="TV Show not found")
    return db_tv_show


@app.delete("/tv-shows/{tv_show_id}", response_model=schemas.TVShow, tags=["tv-shows"])
async def delete_tv_show(tv_show_id: int, db: Session = Depends(get_db)):
    db_tv_show = crud.delete_tv_show(db, tv_show_id)
    if db_tv_show is None:
        raise HTTPException(status_code=404, detail="TV Show not found")
    return db_tv_show
