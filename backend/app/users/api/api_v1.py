from fastapi import APIRouter
from app.config import settings
from app.authentication.auth_router import auth_router
from app.users.schemas import (
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
    router=auth_router.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
