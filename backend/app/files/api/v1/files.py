from fastapi import APIRouter
from app.config import settings

router = APIRouter(
    prefix=settings.api.v1.files,
    tags=["Files"],
)
