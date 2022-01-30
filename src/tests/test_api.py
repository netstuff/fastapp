"""API tests."""

import pytest

from fastapi import status
from httpx import AsyncClient


async def test_api_status(client: AsyncClient):
    """Test API status info."""
    response = await client.get('/')
    assert response.status_code == status.HTTP_200_OK
