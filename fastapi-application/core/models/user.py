from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from typing import TYPE_CHECKING
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from core.types.user_id import UserIdType
from .base import Base
from .mixins import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import (
        AsyncSession,
    )


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    username: Mapped[str]

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
