import secrets
from fastapi import Request
from sqladmin.authentication import AuthenticationBackend
from core.config import settings


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        if (
            form.get("username", "") == settings.superuser.email
            and form.get("password", "") == settings.superuser.password
        ):
            token = secrets.token_hex()
            request.session.update({"access_token": token})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("access_token")

        if not token:
            return False
        return True
