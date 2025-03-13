from fastapi import (
    APIRouter,
)
from core.config import settings
from core.users.api.v1 import users_router
from core.movies.api.v1 import movies_router
from core.authentication.api.v1 import auth_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(users_router)
router.include_router(movies_router)
router.include_router(auth_router)
