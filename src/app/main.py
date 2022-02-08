"""Application main module."""

from app.routes.base import router as base_router
from fastapi import FastAPI


app = FastAPI()

app.include_router(base_router)


@app.on_event("startup")
async def startup_event() -> None:
    """On system starting up."""


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """On system shutdown."""
