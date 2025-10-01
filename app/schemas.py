from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_year: int
    rating: Optional[float] = 0.0

class MovieCreate(MovieBase):
    pass

class MovieUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    release_year: Optional[int]
    rating: Optional[float]

class MovieOut(MovieBase):
    id: int
    created_at: datetime
    updated_at: datetime
 
    class Config:
        from_attributes = True
