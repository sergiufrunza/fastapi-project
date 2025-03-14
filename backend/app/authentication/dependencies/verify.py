from app.authentication.api.v1 import fastapi_users_router

is_authenticated = fastapi_users_router.current_user(active=True)
is_super_user = fastapi_users_router.current_user(active=True, superuser=True)
