"""Pytest root configuration."""

import typing as T

import pytest
from httpx import AsyncClient

from app.main import app


@pytest.fixture()
async def http_client() -> T.AsyncGenerator:
    """Asynchronious HTTP-client."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
