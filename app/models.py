from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

# 🔹 Association table for Movie <-> Genre (many-to-many)
movie_genre = Table(
    "movie_genre",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),
)

# 🔹 Association table for Movie <-> Actor (many-to-many)
movie_actor = Table(
    "movie_actor",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    Column("actor_id", Integer, ForeignKey("actors.id"), primary_key=True),
)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, unique=True)  # prevent duplicates
    description = Column(Text, nullable=True)
    release_year = Column(Integer, nullable=False)
    duration_minutes = Column(Integer, nullable=True)  # e.g., 120 min
    rating = Column(Float, default=0.0)
    vote_count = Column(Integer, default=0)  # IMDb-style votes
    language = Column(String(50), default="English")
    country = Column(String(100), nullable=True)
    budget = Column(Float, nullable=True)
    revenue = Column(Float, nullable=True)
    is_deleted = Column(Boolean, default=False)
    is_trending = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 🔹 Relationships
    genres = relationship("Genre", secondary=movie_genre, back_populates="movies")
    actors = relationship("Actor", secondary=movie_actor, back_populates="movies")
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=True)
    director = relationship("Director", back_populates="movies")

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    movies = relationship("Movie", secondary=movie_genre, back_populates="genres")

class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    birth_year = Column(Integer, nullable=True)

    movies = relationship("Movie", secondary=movie_actor, back_populates="actors")

class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    movies = relationship("Movie", back_populates="director")
