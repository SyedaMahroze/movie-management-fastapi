from fastapi import FastAPI
from app.routers import movies

app = FastAPI(title="Movie CRUD API")
app.include_router(movies.router)
