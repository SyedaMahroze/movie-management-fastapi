Perfect! That adds another important feature: **Watchlist**. I can update the README to include this as well. Here’s the revised version:

---

# 🎬 Movie Management System

A **FastAPI** + **PostgreSQL** system for managing movies, users, subscriptions, reviews, and watchlists. The project provides a RESTful API to handle movie data, user management, subscriptions, reviews, and watchlists.

---

## **Features**

* **Movies Management**: Add, update, delete, and fetch movies
* **User Management**: Register and retrieve users
* **Subscriptions**: Users can subscribe to different plans
* **Reviews**: Users can submit reviews for movies
* **Watchlist**: Users can add movies to their personal watchlist
* **Relational Data**:

  * Users ↔ Subscriptions (one-to-many)
  * Users ↔ Reviews (one-to-many)
  * Users ↔ Watchlist (many-to-many with movies)
  * Movies ↔ Reviews (one-to-many)
* **FastAPI Swagger UI** for interactive API docs
* **Database**: PostgreSQL with SQLAlchemy ORM
* **Testing**: Pytest for all endpoints

---

## **Tech Stack**

* **Backend**: FastAPI
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Migrations**: Alembic
* **Testing**: Pytest
* **API Documentation**: Swagger UI & Redoc

---

## **Database Models**

1. **User** – Stores user information (name, email, etc.)
2. **Movie** – Stores movie details (title, description, release date, etc.)
3. **Subscription** – Tracks user subscriptions and plans
4. **Review** – Stores user reviews for movies, linked to both `User` and `Movie`
5. **Watchlist** – Stores movies added to a user's watchlist

**Relationships:**

* One `User` can have multiple `Subscriptions`
* One `User` can write multiple `Reviews`
* One `Movie` can have multiple `Reviews`
* Many-to-many relationship between `User` and `Movie` for **Watchlist**

---

## **Installation**

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

2. **Set up a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up PostgreSQL**

   * Create a database, e.g., `movie_db`
   * Update `.env` with your database credentials:

```
DATABASE_URL=postgresql://username:password@localhost:5432/movie_db
```

5. **Run database migrations**

```bash
alembic upgrade head
```

6. **Start the FastAPI server**

```bash
uvicorn app.main:app --reload
```

---


## **Endpoints Examples**

### **Users**

* `POST /users/` – Create a new user
* `GET /users/` – Get all users

### **Movies**

* `POST /movies/` – Add a movie
* `GET /movies/` – Retrieve all movies
* `PUT /movies/{id}` – Update movie info
*  `GET /movies/movie/{movie_title}` – Get reviews for a specific movie
  

### **Subscriptions**

* `POST /subscriptions/` – Add subscription for a user
* `GET /subscriptions/` – Get all subscriptions

### **Reviews**

* `POST /reviews/` – Add a review for a movie by a user
* `GET /reviews/` – Get reviews for a movie


### **Watchlist**

* `POST /watchlist/` – Add a movie to a user's watchlist
* `GET /watchlist/{user_id}` – Get all movies in a user's watchlist


---



## **Contribution Guidelines**

1. Fork the repository
2. Create a branch:

```bash
git checkout -b feature-name
```

3. Make changes and commit:

```bash
git commit -m "Add feature"
```

4. Push to your branch:

```bash
git push origin feature-name
```

5. Open a Pull Request

---
