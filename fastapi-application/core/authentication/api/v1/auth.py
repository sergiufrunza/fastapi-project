from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from core.users.models import User
from core.types.user_id import UserIdType
from core.users.dependencies import get_user_manager
from core.authentication.dependencies import authentication_backend


from core.config import settings
from core.users.schemas import (
    UserRead,
    UserCreate,
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

fastapi_users_router = FastAPIUsers[User, UserIdType](
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
