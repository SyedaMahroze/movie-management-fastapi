from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

"""Database configuration with sensible defaults.

If DATABASE_URL is not provided, fall back to a local SQLite database so the
application can run without external dependencies.
"""

# Read database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Fallback to SQLite if not provided
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./app.db"

# Setup database engine and session
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},  # required for SQLite with threads
    )
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,  # keep attributes available after commit/close
    bind=engine,
)
Base = declarative_base()

# Database dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
