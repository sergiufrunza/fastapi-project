from fastapi import APIRouter

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
