from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import Base
from .mixins import IdIntPkMixin


class User(IdIntPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
