from sqlalchemy import Column, Integer, String, Text, Float, Date, Boolean
from app.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    genre = Column(String(100))
    language = Column(String(50))
    release_year = Column(Integer)
    duration = Column(Integer)
    rating = Column(Float)
    description = Column(Text)
    video_url = Column(String)
    poster_url = Column(String)
    status = Column(Boolean, default=True)
