"""
Pydantic models (schemas) for the StreamTracker API.
These define the shape of data accepted/returned by the API.
"""
from typing import Optional, List
from pydantic import BaseModel, Field


class MovieBase(BaseModel):
    title: str = Field(..., description="Title of the movie or book")
    director: str = Field(..., description="Director or author")
    year: int = Field(..., ge=0, description="Year of release or publication")
    rating: Optional[int] = Field(
        None, ge=0, le=10, description="Rating out of 10 (0-10)"
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
    rating: Optional[int] = Field(None, ge=0, le=10)
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
    rating: Optional[int] = Field(None, ge=0, le=10, description="Rating out of 10 (0-10)")
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
    rating: Optional[int] = Field(None, ge=0, le=10)
    watched: Optional[bool] = None
    review: Optional[str] = None
    poster_url: Optional[str] = None


class TVShow(TVShowBase):
    id: int

    class Config:
        from_attributes = True


# Export/Import schemas
class ExportData(BaseModel):
    """Schema for exporting all data from StreamTracker"""
    movies: List[Movie] = Field(..., description="List of all movies")
    tv_shows: List[TVShow] = Field(..., description="List of all TV shows")
    export_metadata: dict = Field(..., description="Export metadata including timestamp and version")
    
    class Config:
        from_attributes = True


class ImportData(BaseModel):
    """Schema for importing data into StreamTracker"""
    movies: List[MovieCreate] = Field(default=[], description="Movies to import")
    tv_shows: List[TVShowCreate] = Field(default=[], description="TV shows to import")
    
    class Config:
        from_attributes = True


class ImportResult(BaseModel):
    """Schema for import operation results"""
    movies_created: int = Field(..., description="Number of movies created")
    movies_updated: int = Field(..., description="Number of movies updated")
    tv_shows_created: int = Field(..., description="Number of TV shows created")
    tv_shows_updated: int = Field(..., description="Number of TV shows updated")
    errors: List[str] = Field(default=[], description="List of errors encountered during import")
    
    class Config:
        from_attributes = True