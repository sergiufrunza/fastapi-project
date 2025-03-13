from fastapi import APIRouter

from api.api_v1.fastapi_users import fastapi_users_router
from api.dependencies.authentication import authentication_backend
from core.config import settings
from core.schemas.user import (
    UserRead,
    UserCreate,
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
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
