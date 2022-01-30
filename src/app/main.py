"""Application main module."""

from fastapi import FastAPI

from .routes.base import router as base_router


app = FastAPI()

app.include_router(base_router)


@app.on_event('startup')
async def startup_event():
    """On system starting up."""
    pass


@app.on_event('shutdown')
async def shutdown_event():
    """On system shutdown."""
    pass
