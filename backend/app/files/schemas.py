from pydantic import BaseModel
import uuid
from app.types import UserIdType


class FileRead(BaseModel):
    id: uuid.UUID


class FileCreate(BaseModel):
    url: str
    user_id: UserIdType
