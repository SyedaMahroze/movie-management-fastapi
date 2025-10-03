# app/core/config.py
from pydantic_settings import BaseSettings  # ✅ updated import

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # load variables from .env file

settings = Settings()
