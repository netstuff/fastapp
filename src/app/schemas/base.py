"""Base schemas."""

from pydantic import BaseModel


class ApiStatusResponse(BaseModel):
    """Index endpoint response."""

    name: str
    version: str
