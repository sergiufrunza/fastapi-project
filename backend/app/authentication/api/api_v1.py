from fastapi import APIRouter
from app.authentication.auth_router import auth_router
from app.authentication.manager import authentication_backend


from app.config import settings
from app.users.schemas import (
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
    router=auth_router.get_auth_router(
        authentication_backend,
    ),
)

# /register
router.include_router(
    router=auth_router.get_register_router(
        UserRead,
        UserCreate,
    ),
)
# /request-verify-token
# /verify
router.include_router(
    router=auth_router.get_verify_router(UserRead),
)

# /forgot-password
# /reset-password
router.include_router(
    router=auth_router.get_reset_password_router(),
)
