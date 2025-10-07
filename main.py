from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, movies, reviews, subscriptions, watchlist
# Ensure models are registered with Base before creating tables
from app import models  # noqa: F401

# Create DB tables automatically after models are imported
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Management API", version="1.0", debug=True)

# Include all routers
app.include_router(users.router)
app.include_router(movies.router)
app.include_router(reviews.router)
app.include_router(subscriptions.router)
app.include_router(watchlist.router)

@app.get("/")
def home():
    return {"message": "Welcome to Movie Management API!"}
