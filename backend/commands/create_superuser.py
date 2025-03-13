import asyncio
import contextlib
import logging
from app.users.dependencies import (
    get_user_manager,
    get_users_db,
)
from app.authentication.user_manager import UserManager
from app.db import (
    db_helper,
    User,
)

from app.users.schemas import UserCreate
from app.config import settings
from fastapi_users.exceptions import UserAlreadyExists

log = logging.getLogger(__name__)
get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    email: str = settings.superuser.email,
    password: str = settings.superuser.password,
    username: str = settings.superuser.username,
    is_active: bool = True,
    is_superuser: bool = True,
    is_verified: bool = True,
):
    user_create = UserCreate(
        email=email,
        password=password,
        username=username,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    try:
        async with db_helper.session_factory() as session:
            async with get_users_db_context(session) as users_db:
                async with get_user_manager_context(users_db) as user_manager:
                    return await create_user(
                        user_manager=user_manager,
                        user_create=user_create,
                    )
    except UserAlreadyExists:
        log.warning("User already exists.")


if __name__ == "__main__":
    asyncio.run(create_superuser())
