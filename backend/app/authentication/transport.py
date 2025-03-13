from fastapi_users.authentication import BearerTransport
from app.config import settings

bearer_transport = BearerTransport(
    tokenUrl=settings.api.bearer_token_url,
)
