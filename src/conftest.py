"""Pytest root configuration."""

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope='module')
def client() -> Generator:
    """Asynchronious HTTP-client."""
    yield TestClient(app)
