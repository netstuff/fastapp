"""Base routes."""

from app.schemas.base import ApiStatusResponse
from app.settings import Settings, get_settings
from fastapi import APIRouter, Depends, Response


router = APIRouter(prefix="")


@router.get("/", response_model=ApiStatusResponse, tags=["common"])
async def get_status(settings: Settings = Depends(get_settings)) -> Response:
    """Index endpoint."""
    return {**settings.poetry.dict()}
