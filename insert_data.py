from sqlalchemy.orm import Session
from app.core.database import engine, Base
from app.models import Movie, Genre, Actor, Director

# 🔹 Create all tables if not already created
Base.metadata.create_all(bind=engine)

# 🔹 Start a session
session = Session(bind=engine)

# ---------- Insert Genres ----------
genre1 = Genre(name="Action")
genre2 = Genre(name="Sci-Fi")
genre3 = Genre(name="Drama")

session.add_all([genre1, genre2, genre3])
session.commit()

# ---------- Insert Actors ----------
actor1 = Actor(name="Leonardo DiCaprio", birth_year=1974)
actor2 = Actor(name="Joseph Gordon-Levitt", birth_year=1981)
actor3 = Actor(name="Elliot Page", birth_year=1987)

session.add_all([actor1, actor2, actor3])
session.commit()

# ---------- Insert Director ----------
director1 = Director(name="Christopher Nolan")

session.add(director1)
session.commit()

# ---------- Insert a Movie ----------
movie1 = Movie(
    title="Inception",
    description="A thief who steals corporate secrets through dreams.",
    release_year=2010,
    duration_minutes=148,
    rating=8.8,
    vote_count=2000,
    language="English",
    country="USA",
    budget=160000000,
    revenue=829895144,
    director=director1,            # 🔹 set relationship
    genres=[genre1, genre2],      # 🔹 set many-to-many
    actors=[actor1, actor2, actor3]
)

session.add(movie1)
session.commit()

print("✅ Data inserted successfully!")

# 🔹 Close session
session.close()
