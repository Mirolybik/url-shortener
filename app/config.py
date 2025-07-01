from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    REDIS_URL: str = "redis://redis:6379/0"
    SHORT_URL_LENGTH: int = 6
    DEFAULT_TTL: int = 3600

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()