import uuid
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import (
    ForeignKey,
    String,
)
from app.types import UserIdType
from app.db.base import Base
from app.mixins import IdUUIDPkMixin
from datetime import datetime


class File(IdUUIDPkMixin, Base):
    url: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[UserIdType] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
