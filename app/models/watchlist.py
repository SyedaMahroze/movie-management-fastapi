from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

watchlist = Table(
    "watchlist",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("movie_id", Integer, ForeignKey("movies.id", ondelete="CASCADE")),
)
