"""Application main module."""
from app.db.connections import close_db, init_db, set_db_in_app
from app.routes.base import router as base_router
from app.settings import settings
from fastapi import FastAPI


app = FastAPI()

app.include_router(base_router)


@app.on_event("startup")
async def startup_event() -> None:
    """On system starting up."""
    engine, session = init_db(settings.postgres.dsn)
    set_db_in_app(app, engine, session)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """On system shutdown."""
    await close_db(app)
