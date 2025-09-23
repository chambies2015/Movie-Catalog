"""
Pydantic models (schemas) for the StreamTracker API.
These define the shape of data accepted/returned by the API.
"""
from typing import Optional
from pydantic import BaseModel, Field


class MovieBase(BaseModel):
    title: str = Field(..., description="Title of the movie or book")
    director: str = Field(..., description="Director or author")
    year: int = Field(..., ge=0, description="Year of release or publication")
    rating: Optional[float] = Field(
        None, ge=0, le=10, description="Rating out of 10"
    )  # rating is now optional
    watched: Optional[bool] = Field(False, description="Whether it has been watched/read")
    review: Optional[str] = Field(None, description="Optional review/notes for the entry")
    poster_url: Optional[str] = Field(None, description="URL of the movie poster")


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    director: Optional[str] = None
    year: Optional[int] = Field(None, ge=0)
    rating: Optional[float] = Field(None, ge=0, le=10)
    watched: Optional[bool] = None
    review: Optional[str] = None
    poster_url: Optional[str] = None


class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True


class TVShowBase(BaseModel):
    title: str = Field(..., description="Title of the TV show")
    year: int = Field(..., ge=0, description="Year of the TV show")
    seasons: Optional[int] = Field(None, ge=0, description="Number of seasons")
    episodes: Optional[int] = Field(None, ge=0, description="Total number of episodes")
    rating: Optional[float] = Field(None, ge=0, le=10, description="Rating out of 10")
    watched: Optional[bool] = Field(False, description="Whether it has been watched")
    review: Optional[str] = Field(None, description="Optional review/notes for the entry")
    poster_url: Optional[str] = Field(None, description="URL of the TV show poster")


class TVShowCreate(TVShowBase):
    pass


class TVShowUpdate(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = Field(None, ge=0)
    seasons: Optional[int] = Field(None, ge=0)
    episodes: Optional[int] = Field(None, ge=0)
    rating: Optional[float] = Field(None, ge=0, le=10)
    watched: Optional[bool] = None
    review: Optional[str] = None
    poster_url: Optional[str] = None


class TVShow(TVShowBase):
    id: int

    class Config:
        from_attributes = True