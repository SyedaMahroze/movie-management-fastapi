# Movie Management API

This is a **FastAPI** project to manage movies, actors, genres, and directors. It supports CRUD operations and relations between movies, actors, genres, and directors.

---

## Features

- **Movies**
  - Create, read, update, and delete movies.
  - Each movie can have multiple genres and actors.
  - Each movie has a director.
  - Track details like release year, duration, rating, budget, and revenue.

- **Actors**
  - Add and manage actors.
  - Link actors to multiple movies.

- **Genres**
  - Add and manage genres.
  - Link genres to multiple movies.

- **Directors**
  - Add and manage directors.
  - Each director can have multiple movies.

- **Search**
  - Search movies by title, actor, director, or genre.

---

## Tech Stack

- **Backend**: FastAPI  
- **Database**: PostgreSQL  
- **ORM**: SQLAlchemy  
- **Migrations**: Alembic  
- **Environment Management**: Python Virtual Environment (`venv`)  

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SyedaMahroze/movie-management-fastapi.git
cd movie-management-fastapi
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create `.env` file with database URL:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/moviedb
```

5. Run migrations:

```bash
alembic upgrade head
```

6. Start the server:

```bash
uvicorn main:app --reload
```

---


## Notes

* Make sure your PostgreSQL server is running and the database exists.
* Use `.gitignore` to avoid uploading sensitive files like `.env` and virtual environments.

```
