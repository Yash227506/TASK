import os
from functools import lru_cache


class Settings:
    def __init__(self) -> None:
        self.app_name = os.getenv("APP_NAME", "Task Manager API")
        database_url = os.getenv(
            "DATABASE_URL",
            "sqlite:///./task_manager.db",
        )
        self.database_url = self._normalize_database_url(database_url)

    @staticmethod
    def _normalize_database_url(database_url: str) -> str:
        if database_url.startswith("postgresql+psycopg2://"):
            return database_url.replace("postgresql+psycopg2://", "postgresql+psycopg://", 1)
        return database_url


@lru_cache
def get_settings() -> Settings:
    return Settings()
