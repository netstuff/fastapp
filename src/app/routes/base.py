"""Base routes."""

from isort import api
from fastapi import APIRouter, Depends

from ..settings import Settings, get_settings
from ..schemas.base import ApiStatusResponse


router = APIRouter(prefix=None)


@router.get("/", response_model=ApiStatusResponse, tags=["common"])
async def get_status(settings: Settings=Depends(get_settings)):
    """Index endpoint."""
    return {**settings.poetry.dict()}
