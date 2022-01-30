"""Application main module."""

from fastapi import FastAPI


app = FastAPI()


@app.on_event('startup')
async def startup_event():
    """On system starting up."""
    pass


@app.on_event('shutdown')
async def shutdown_event():
    """On system shutdown."""
    pass
