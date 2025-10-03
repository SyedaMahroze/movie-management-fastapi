from sqlalchemy.orm import Session
from app.models import Movie, Actor, Director, Genre
from app import schemas

# -----------------------
# Search Functions
# -----------------------

def get_movie_by_title(db: Session, title: str):
    """Search single movie by title (case-insensitive, partial match)."""
    return db.query(Movie).filter(Movie.title.ilike(f"%{title}%")).first()


def get_movies_by_actor(db: Session, actor_name: str):
    """Get all movies where given actor played."""
    return (
        db.query(Movie)
        .join(Movie.actors)
        .filter(Actor.name.ilike(f"%{actor_name}%"))
        .all()
    )


def get_movies_by_director(db: Session, director_name: str):
    """Get all movies directed by given director."""
    return (
        db.query(Movie)
        .join(Movie.director)
        .filter(Director.name.ilike(f"%{director_name}%"))
        .all()
    )


def get_movies_by_genre(db: Session, genre_name: str):
    """Get all movies belonging to a given genre."""
    return (
        db.query(Movie)
        .join(Movie.genres)
        .filter(Genre.name.ilike(f"%{genre_name}%"))
        .all()
    )


# -----------------------
# CRUD Functions
# -----------------------

def create_movie(db: Session, movie: schemas.MovieCreate):
    """Create a new movie with optional genres & actors."""
    db_movie = Movie(
        title=movie.title,
        description=movie.description,
        release_year=movie.release_year,
        duration_minutes=movie.duration_minutes,
        rating=movie.rating,
        vote_count=movie.vote_count,
        language=movie.language,
        country=movie.country,
        budget=movie.budget,
        revenue=movie.revenue,
        is_trending=movie.is_trending,
        director_id=movie.director_id,
    )

    # Attach genres if provided
    if movie.genres:
        db_movie.genres = db.query(Genre).filter(Genre.id.in_(movie.genres)).all()

    # Attach actors if provided
    if movie.actors:
        db_movie.actors = db.query(Actor).filter(Actor.id.in_(movie.actors)).all()

    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    """Return paginated list of movies."""
    return db.query(Movie).offset(skip).limit(limit).all()


def get_movie(db: Session, movie_id: int):
    """Return a single movie by ID."""
    return db.query(Movie).filter(Movie.id == movie_id).first()


def update_movie(db: Session, movie_id: int, movie: schemas.MovieUpdate):
    """Update movie info and relationships (actors, genres)."""
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        return None

    update_data = movie.dict(exclude_unset=True)

    # Update normal fields
    for key, value in update_data.items():
        if key not in ["genres", "actors"]:
            setattr(db_movie, key, value)

    # Update genres
    if movie.genres is not None:
        db_movie.genres = db.query(Genre).filter(Genre.id.in_(movie.genres)).all()

    # Update actors
    if movie.actors is not None:
        db_movie.actors = db.query(Actor).filter(Actor.id.in_(movie.actors)).all()

    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int):
    """Delete a movie by ID."""
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        return False
    db.delete(db_movie)
    db.commit()
    return True
