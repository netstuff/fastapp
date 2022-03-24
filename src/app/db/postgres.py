from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker


def create_engine(connection_string: str) -> AsyncEngine:
    """Create engine."""
    return create_async_engine(connection_string)


def create_sessionmaker(
    engine: AsyncEngine, expire_on_commit: bool = False,
) -> sessionmaker:
    """Create sessionmaker."""
    return sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=expire_on_commit,
    )
