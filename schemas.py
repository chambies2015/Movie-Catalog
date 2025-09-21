"""
Pydantic models (schemas) for the Movie Catalog API.
These define the shape of data accepted/returned by the API.
"""
from typing import Optional
from pydantic import BaseModel, Field


class MovieBase(BaseModel):
    title: str = Field(..., description="Title of the movie or book")
    director: str = Field(..., description="Director or author")
    year: int = Field(..., ge=0, description="Year of release or publication")
    rating: float = Field(..., ge=0, le=10, description="Rating out of 10")
    watched: Optional[bool] = Field(False, description="Whether it has been watched/read")


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    director: Optional[str] = None
    year: Optional[int] = Field(None, ge=0)
    rating: Optional[float] = Field(None, ge=0, le=10)
    watched: Optional[bool] = None


class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True
