from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime
from typing import Optional

class MovieBase(BaseModel):
    title: str
    genre: Optional[str] = None
    language: Optional[str] = None
    release_year: Optional[int] = None
    duration: Optional[int] = None
    rating: Optional[float] = None
    description: Optional[str] = None
    video_url: Optional[str] = None
    poster_url: Optional[str] = None
    status: Optional[bool] = True

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
