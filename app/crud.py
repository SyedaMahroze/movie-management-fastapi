from sqlalchemy.orm import Session
from app import schemas
from app.model import movie as models   

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id, models.Movie.is_deleted == False).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).filter(models.Movie.is_deleted == False).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie(db: Session, movie_id: int, movie_update: schemas.MovieUpdate):
    db_movie = get_movie(db, movie_id)
    if not db_movie:
        return None
    for field, value in movie_update.dict(exclude_unset=True).items():
        setattr(db_movie, field, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = get_movie(db, movie_id)
    if not db_movie:
        return False
    # soft delete
    db_movie.is_deleted = True
    db.commit()
    return True
