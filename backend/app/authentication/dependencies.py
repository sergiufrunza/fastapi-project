from app.authentication.auth_router import auth_router

is_authenticated = auth_router.current_user(active=True)
is_super_user = auth_router.current_user(active=True, superuser=True)
