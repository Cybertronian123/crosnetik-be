from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str = "CrosNetik API"
    env: str = "dev"

    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "crosnetik"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()