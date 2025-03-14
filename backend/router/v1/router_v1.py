from fastapi import (
    APIRouter,
)
from app.config import settings
from app.users.api.v1 import users_router
from app.authentication.api.v1 import auth_router
from app.files.api.v1 import files_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(files_router)
