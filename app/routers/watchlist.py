from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.models.movie import Movie
from app.models.watchlist import watchlist

router = APIRouter(prefix="/watchlist", tags=["Watchlist"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}/{movie_id}")
def add_to_watchlist(user_id: int, movie_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    movie = db.query(Movie).get(movie_id)
    if not user or not movie:
        raise HTTPException(status_code=404, detail="User or Movie not found")

    db.execute(watchlist.insert().values(user_id=user_id, movie_id=movie_id))
    db.commit()
    return {"message": f"{movie.title} added to watchlist"}

@router.get("/{user_id}")
def get_watchlist(user_id: int, db: Session = Depends(get_db)):
    result = (
        db.query(Movie)
        .join(watchlist, Movie.id == watchlist.c.movie_id)
        .filter(watchlist.c.user_id == user_id)
        .all()
    )
    return result
