from .manager import (
    get_auth_manager,
    authentication_backend,
)
from fastapi_users import (
    FastAPIUsers,
)
from app.users.models import User
import uuid

auth_router = FastAPIUsers[User, uuid.UUID](
    get_auth_manager,
    [authentication_backend],
)
