from typing import List, Optional
from pydantic import BaseModel

# ---------- GENRE ----------
class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class GenreOut(GenreBase):
    id: int
    class Config:
        from_attributes = True  # updated for Pydantic v2

# ---------- ACTOR ----------
class ActorBase(BaseModel):
    name: str
    birth_year: Optional[int] = None

class ActorCreate(ActorBase):
    pass

class ActorOut(ActorBase):
    id: int
    class Config:
        from_attributes = True

# ---------- DIRECTOR ----------
class DirectorBase(BaseModel):
    name: str

class DirectorCreate(DirectorBase):
    pass

class DirectorOut(DirectorBase):
    id: int
    class Config:
        from_attributes = True

# ---------- MOVIE ----------
class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_year: int
    duration_minutes: Optional[int] = None
    rating: float = 0.0
    vote_count: int = 0
    language: str = "English"
    country: Optional[str] = None
    budget: Optional[float] = None
    revenue: Optional[float] = None
    is_trending: bool = False

class MovieCreate(MovieBase):
    genres: Optional[List[int]] = []     # list of genre IDs
    actors: Optional[List[int]] = []     # list of actor IDs
    director_id: Optional[int] = None

class MovieUpdate(MovieBase):
    title: Optional[str] = None
    release_year: Optional[int] = None
    duration_minutes: Optional[int] = None
    rating: Optional[float] = None
    vote_count: Optional[int] = None
    is_trending: Optional[bool] = None
    genres: Optional[List[int]] = []
    actors: Optional[List[int]] = []
    director_id: Optional[int] = None

class MovieOut(MovieBase):
    id: int
    genres: List[GenreOut] = []
    actors: List[ActorOut] = []
    director: Optional[DirectorOut] = None

    class Config:
        from_attributes = True
