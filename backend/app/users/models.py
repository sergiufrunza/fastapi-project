from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from typing import TYPE_CHECKING
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyUserDatabase,
)
from app.db import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import (
        AsyncSession,
    )


class User(Base, SQLAlchemyBaseUserTableUUID):
    username: Mapped[str]

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
