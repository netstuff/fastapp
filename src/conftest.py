"""Pytest root configuration."""

import typing as T

import pytest
from httpx import AsyncClient

from app.main import app


@pytest.fixture
@pytest.mark.asyncio
async def client() -> T.Generator:
    """Asynchronious HTTP-client."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
