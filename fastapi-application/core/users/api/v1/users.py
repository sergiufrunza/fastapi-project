from fastapi import APIRouter
from core.config import settings
from core.authentication.api.v1 import fastapi_users_router
from core.users.schemas import (
    UserRead,
    UserUpdate,
)

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)
# /me
# /{id}
router.include_router(
    router=fastapi_users_router.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
