from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.security import HTTPBearer
from app.config import settings
from app.users.api import user_router_v1
from app.authentication.api import auth_router_v1
from app.files.api import files_router_v1
from app.gpt.api import gpt_router_v1

router_v1 = APIRouter(
    prefix=settings.api.v1.prefix,
)
router_v1.include_router(auth_router_v1)
router_v1.include_router(user_router_v1)
router_v1.include_router(files_router_v1)
router_v1.include_router(gpt_router_v1)


http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(router_v1)
