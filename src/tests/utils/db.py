from app.db.models.base import Base
from fastapi import FastAPI


async def create_db(app: FastAPI) -> None:
    """Create DB."""
    async with app.db_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


async def clear_db(app: FastAPI) -> None:
    """Clear DB."""
    async with app.db_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
