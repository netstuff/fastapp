"""Pytest root configuration."""

import typing as T

import pytest
from httpx import AsyncClient

from app.db.connections import init_db, set_db_in_app
from app.main import app
from app.settings import settings
from fastapi import FastAPI
from tests.utils.db import clear_db, create_db


@pytest.fixture(name="app_test")
async def app_test() -> T.AsyncGenerator:
    """Connection from BD."""
    engine, session = init_db(settings.postgres.dsn)
    set_db_in_app(app, engine, session)
    await create_db(app)
    yield app
    await clear_db(app)


@pytest.fixture()
async def http_client(app_test: FastAPI) -> T.AsyncGenerator:  # noqa: WPS442
    """Asynchronious HTTP-client."""
    async with AsyncClient(
        app=app_test,
        base_url="http://test",  # noqa: D103
    ) as client:  # noqa: WPS442
        yield client
