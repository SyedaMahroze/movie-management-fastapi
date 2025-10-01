from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.core.database import get_db

router = APIRouter(prefix="/movies", tags=["movies"])

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
