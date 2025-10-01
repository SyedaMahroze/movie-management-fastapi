from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean
from datetime import datetime
from app.core.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    release_year = Column(Integer, nullable=False)
    rating = Column(Float, default=0.0)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


