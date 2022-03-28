"""Base application settings."""

import typing as T
from functools import lru_cache
from pathlib import Path

import toml
from pydantic import (
    BaseModel,
    BaseSettings,
    PostgresDsn,
    ValidationError,
    validator,
)

from app.constants import ROOT_DIR


PYPROJ: Path = ROOT_DIR / "pyproject.toml"
POETRY: T.Dict[str, str] = toml.load(PYPROJ)["tool"]["poetry"]


class PoetryProject(BaseModel):
    """Project settings."""

    name: str
    version: str


class PostgresSettings(BaseModel):
    """PostgreSQL settings."""

    dsn: PostgresDsn

    @validator("dsn")
    def validate_dsn(cls, value: PostgresDsn) -> PostgresDsn:
        """Check DSN async option."""
        if "asyncpg" not in value.scheme:
            raise ValueError("You should to use asyncpg option in DSN scheme")

        return value


class Settings(BaseSettings):
    """Base settings."""

    poetry: PoetryProject = PoetryProject(**POETRY)
    postgres: PostgresSettings

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"


@lru_cache()
def get_settings() -> Settings:
    """Get settings."""
    return Settings()
