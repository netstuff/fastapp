"""Base application settings."""

import typing as T
from functools import lru_cache
from pathlib import Path

import toml
from pydantic import BaseModel, BaseSettings

from app.constants import ROOT_DIR


PYPROJ: Path = ROOT_DIR / "pyproject.toml"
POETRY: T.Dict[str, str] = toml.load(PYPROJ)["tool"]["poetry"]


class PoetryProject(BaseModel):
    """Project settings."""

    name: str
    version: str


class Settings(BaseSettings):
    """Base settings."""

    poetry: PoetryProject = PoetryProject(**POETRY)

    class Config:
        env_file = ".env"
        env_prefix = POETRY["name"].upper().replace("-", "_")


@lru_cache()
def get_settings() -> Settings:
    """Get settings."""
    return Settings()
