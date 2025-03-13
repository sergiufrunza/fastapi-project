from fastapi import (
    APIRouter,
    Depends,
)
from app.config import settings
from .v1 import router_v1
from fastapi.security import HTTPBearer

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(router_v1)
