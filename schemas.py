"""
Pydantic models (schemas) for the Movie Tracker API.
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


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    director: Optional[str] = None
    year: Optional[int] = Field(None, ge=0)
    rating: Optional[float] = Field(None, ge=0, le=10)
    watched: Optional[bool] = None
    review: Optional[str] = None


class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True
