from fastapi_users import FastAPIUsers

from core.models import User
from core.types.user_id import UserIdType

from api.dependencies.authentication import get_user_manager
from api.dependencies.authentication import authentication_backend

fastapi_users_router = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

is_authenticated = fastapi_users_router.current_user(active=True)
is_super_user = fastapi_users_router.current_user(active=True, superuser=True)
