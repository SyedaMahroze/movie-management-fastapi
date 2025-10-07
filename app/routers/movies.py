from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieResponse

router = APIRouter(prefix="/movies", tags=["Movies"])

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Movie
@router.post("/", response_model=MovieResponse)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

# Get All Movies
@router.get("/", response_model=list[MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()

# Get Movie by ID
@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

# Search Movies
@router.get("/search/", response_model=list[MovieResponse])
def search_movies(query: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    """
    Search movies by title or description (case-insensitive)
    """
    results = db.query(Movie).filter(
        (Movie.title.ilike(f"%{query}%")) |
        (Movie.description.ilike(f"%{query}%"))
    ).all()

    if not results:
        raise HTTPException(status_code=404, detail="No movies found matching your search")

    return results
