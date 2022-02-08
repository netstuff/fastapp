"""API tests."""

from httpx import AsyncClient

from fastapi import status


async def test_api_status(http_client: AsyncClient) -> None:
    """Test API status info."""
    response = await http_client.get("/")
    assert response.status_code is status.HTTP_200_OK
