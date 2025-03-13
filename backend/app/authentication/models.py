from typing import TYPE_CHECKING
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTableUUID,
    SQLAlchemyAccessTokenDatabase,
)
from sqlalchemy import (
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.db.base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import (
        AsyncSession,
    )


class AccessToken(Base, SQLAlchemyBaseAccessTokenTableUUID):
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
