from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI: str
    DOWNLOAD_PATH: str
    DOWNLOAD_LIMIT: int
    HOST: str

    class Config:
        env_file = "/app/.env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
