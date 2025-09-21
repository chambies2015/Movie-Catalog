"""
Entry point for the Movie Tracker API.
Provides CRUD endpoints for managing movies or books.
"""
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import schemas
from database import Base, SessionLocal, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="Movie Tracker API", description="Manage your movies and books", version="0.1.0")

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
    return {"message": "Movie Tracker API is running \U0001f680"}


@app.get("/movies/", response_model=List[schemas.Movie], tags=["movies"])
async def list_movies(search: Optional[str] = None, sort_by: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_movies(db, search=search, sort_by=sort_by)


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


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
