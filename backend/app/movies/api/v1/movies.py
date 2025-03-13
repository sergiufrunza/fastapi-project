from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import settings
from app.db import db_helper
from app.movies import crud as movies_crud

from app.movies.schemas import (
    MovieRead,
)

router = APIRouter(
    prefix=settings.api.v1.movies,
    tags=["Movies"],
)


@router.get("", response_model=list[MovieRead])
async def get_movies(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    movies = await movies_crud.get_all_movies(session=session)
    return movies


@router.get("/{id}", response_model=MovieRead)
async def get_movie(
    movie_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    movie = await movies_crud.get_movie(session=session, movie_id=movie_id)
    return movie
