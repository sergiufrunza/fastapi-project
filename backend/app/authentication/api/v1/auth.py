from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.db import User
from app.users.dependencies import get_user_manager
from app.authentication.dependencies import authentication_backend
import uuid

from app.config import settings
from app.users.schemas import (
    UserRead,
    UserCreate,
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

fastapi_users_router = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [authentication_backend],
)

# /login
# /logout
router.include_router(
    router=fastapi_users_router.get_auth_router(
        authentication_backend,
        # requires_verification=True,
    ),
)

# /register
router.include_router(
    router=fastapi_users_router.get_register_router(
        UserRead,
        UserCreate,
    ),
)
# /request-verify-token
# /verify
router.include_router(
    router=fastapi_users_router.get_verify_router(UserRead),
)

# /forgot-password
# /reset-password
router.include_router(
    router=fastapi_users_router.get_reset_password_router(),
)

is_authenticated = fastapi_users_router.current_user(active=True)
is_super_user = fastapi_users_router.current_user(active=True, superuser=True)
