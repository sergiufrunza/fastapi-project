__all__ = (
    "auth_router",
    "fastapi_users_router",
)

from .auth import router as auth_router
from .auth import (
    fastapi_users_router,
)
