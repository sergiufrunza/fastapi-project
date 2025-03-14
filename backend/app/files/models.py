from typing import TYPE_CHECKING
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import String
from app.db.base import Base
from app.mixins import IdUUIDPkMixin
from datetime import datetime


class File(IdUUIDPkMixin, Base):
    url: Mapped[String] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
