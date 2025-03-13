from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
import uuid
from sqlalchemy.dialects.postgresql import UUID as PgUUID


class IdUUIDPkMixin:
    id: Mapped[uuid.UUID] = mapped_column(
        PgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
