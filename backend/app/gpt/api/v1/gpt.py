import uuid
from typing import Annotated, TYPE_CHECKING
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from app.gpt.schemas import (
    QuizRead,
)
from sqlalchemy.future import select
from app.files.models import File as FileModel
from app.config import settings
from app.db import db_helper
from app.authentication.dependencies.verify import is_authenticated
from app.gpt.services import get_quiz as get_gpt_quiz

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from app.users.schemas import UserRead


router = APIRouter(
    prefix=settings.api.v1.gpt,
    tags=["GPT"],
)


@router.get("/{file_id}", response_model=QuizRead)
async def get_quiz(
    file_id: uuid.UUID,
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
    user: Annotated["UserRead", Depends(is_authenticated)],
) -> QuizRead:

    result = await session.execute(
        select(FileModel).filter(FileModel.id == file_id, FileModel.user_id == user.id)
    )
    file_result = result.scalars().first()
    if not file_result:
        raise HTTPException(status_code=404, detail="File not found")
    quiz = await get_gpt_quiz(file_result.url)
    response = QuizRead(quiz=quiz)
    return response
