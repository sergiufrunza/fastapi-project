from pydantic import BaseModel
import uuid


class FileRead(BaseModel):
    id: uuid.UUID



class FileCreate(BaseModel):
    url: str

