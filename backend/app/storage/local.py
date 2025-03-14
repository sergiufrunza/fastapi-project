from typing import TYPE_CHECKING
import uuid
import aiofiles
from app.config import settings
from pathlib import Path


if TYPE_CHECKING:
    from fastapi import UploadFile

UPLOAD_DIR = Path(settings.local_storage.dir)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


async def save_upload_file(upload_file: "UploadFile") -> tuple[Path, uuid.UUID]:
    file_id = uuid.uuid4()
    filename = f"{file_id}.pdf"
    file_location = UPLOAD_DIR / filename
    async with aiofiles.open(file_location, "wb") as f:
        await f.write(await upload_file.read())
    return file_location, file_id
