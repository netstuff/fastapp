from typing import Tuple

from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from app.db.postgres import create_engine, create_sessionmaker
from fastapi import FastAPI


def init_db(dsn: PostgresDsn) -> Tuple[AsyncEngine, sessionmaker]:
    """Create engine and sessionmaker."""
    engine = create_engine(dsn)
    session = create_sessionmaker(engine)

    return (engine, session)


async def close_db(app: FastAPI) -> None:
    """Close DB."""
    await app.db_engine.dispose()


def set_db_in_app(
    app: FastAPI, engine: AsyncEngine, session: sessionmaker,
) -> None:
    """Set DB connection in app."""
    app.db_engine = engine
    app.db_session = session
