from typing import Sequence

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Movie


async def get_all_movies(
    session: AsyncSession,
) -> Sequence[Movie]:
    stmt = select(Movie).order_by(Movie.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_movie(
    session: AsyncSession,
    movie_id: int,
) -> Movie | None:
    return await session.get(Movie, movie_id)
