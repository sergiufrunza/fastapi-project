from sqlalchemy.orm import (
    Mapped,
)

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from app.db import Base


class User(Base, SQLAlchemyBaseUserTableUUID):
    username: Mapped[str]
