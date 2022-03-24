from abc import ABC, abstractmethod
from typing import TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.base import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(ABC):
    """Base repository."""

    def __init__(self, session: AsyncSession):
        """Init session."""
        self.session: AsyncSession = session

    @property
    @abstractmethod
    def model(self) -> ModelType:
        """Repository model."""
