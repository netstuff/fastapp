"""Base application settings."""

import typing as T
from functools import lru_cache

import toml
from pydantic import BaseModel, BaseSettings

from ..constants import ROOT_DIR


POETRY: T.Dict[str, str] = toml.load(ROOT_DIR / "pyproject.toml")["tool"]["poetry"]


class PoetryProject(BaseModel):
    """Project settings."""

    name: str
    version: str


class Settings(BaseSettings):
    """Base settings."""

    poetry: PoetryProject = PoetryProject(**POETRY)

    class Config:
        env_file = ".env"
        env_prefix = POETRY["name"].upper().replace('-', '_')


@lru_cache()
def get_settings():
    """Get settings."""
    return Settings()
