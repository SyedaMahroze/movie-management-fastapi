from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.core.database import get_db

router = APIRouter(prefix="/movies", tags=["movies"])

# ----------------------
# CRUD Operations
# ----------------------

@router.post("/", response_model=schemas.MovieOut, status_code=status.HTTP_201_CREATED)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.get("/", response_model=List[schemas.MovieOut])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip=skip, limit=limit)

@router.get("/{movie_id}", response_model=schemas.MovieOut)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.put("/{movie_id}", response_model=schemas.MovieOut)
def update_movie(movie_id: int, movie: schemas.MovieUpdate, db: Session = Depends(get_db)):
    updated = crud.update_movie(db, movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated

@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_movie(db, movie_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted"}


# ----------------------
# Search Routes
# ----------------------

@router.get("/search/title/{title}", response_model=schemas.MovieOut)
def search_by_title(title: str, db: Session = Depends(get_db)):
    movie = crud.get_movie_by_title(db, title)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.get("/search/actor/{actor_name}", response_model=List[schemas.MovieOut])
def search_by_actor(actor_name: str, db: Session = Depends(get_db)):
    movies = crud.get_movies_by_actor(db, actor_name)
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found for this actor")
    return movies

@router.get("/search/director/{director_name}", response_model=List[schemas.MovieOut])
def search_by_director(director_name: str, db: Session = Depends(get_db)):
    movies = crud.get_movies_by_director(db, director_name)
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found for this director")
    return movies

@router.get("/search/genre/{genre_name}", response_model=List[schemas.MovieOut])
def search_by_genre(genre_name: str, db: Session = Depends(get_db)):
    movies = crud.get_movies_by_genre(db, genre_name)
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found for this genre")
    return movies
