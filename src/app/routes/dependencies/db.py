from collections.abc import AsyncGenerator
from typing import Callable, Type

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.base import BaseRepository
from fastapi import Depends, Request


Repository = Callable[[AsyncSession], BaseRepository]


def get_repository(repository_type: Type[BaseRepository]) -> Repository:
    """Get repository."""

    async def _get_repo(  # noqa: WPS430
        session: AsyncSession = Depends(
            _get_session,
        ),
    ) -> BaseRepository:
        return repository_type(session)

    return _get_repo


async def _get_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    """Get session."""
    async with request.app.db_session as session, session.begin():  # noqa: WPS316, E501
        yield session
