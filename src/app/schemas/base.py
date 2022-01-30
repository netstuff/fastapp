"""Base schemas."""

from pydantic import BaseModel

from ..settings.base import PoetrySettings


class ApiStatusResponse(BaseModel):
    """Index endpoint response."""

    name: PoetrySettings.name
    version: PoetrySettings.version
