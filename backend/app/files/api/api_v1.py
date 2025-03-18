from typing import Annotated, TYPE_CHECKING
from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException,
)
from app.files.schemas import (
    FileRead,
    FileCreate,
)
from app.config import settings
from app.db import db_helper
from app.files.models import File as FileModel
from app.authentication.dependencies.verify import is_authenticated
from app.storage.local import save_upload_file

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from app.users.schemas import UserRead


router = APIRouter(
    prefix=settings.api.v1.files,
    tags=["Files"],
)


@router.post("/upload", response_model=FileRead)
async def upload_file_movies(
    file: Annotated[UploadFile, File(...)],
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
    user: Annotated["UserRead", Depends(is_authenticated)],
) -> File:
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")
    url, file_id = await save_upload_file(file)
    file_validator = FileCreate(
        url=str(url),
        user_id=user.id,
    )

    new_file = FileModel(
        id=file_id,
        url=file_validator.url,
        user_id=file_validator.user_id,
    )
    session.add(new_file)
    await session.commit()
    await session.refresh(new_file)
    return new_file
