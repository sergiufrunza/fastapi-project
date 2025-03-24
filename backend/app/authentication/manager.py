from typing import (
    Optional,
    TYPE_CHECKING,
    Annotated,
)
from fastapi import Depends
from fastapi_users import (
    BaseUserManager,
    UUIDIDMixin,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
)
from app.config import settings
from app.db import (
    db_helper,
    User,
)

import uuid
import logging


if TYPE_CHECKING:
    from fastapi import Request
    from sqlalchemy.ext.asyncio import AsyncSession
    from app.authentication.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase

log = logging.getLogger(__name__)


class AuthManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has registered.",
            user.id,
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token,
        )


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield SQLAlchemyUserDatabase(session, User)


async def get_access_tokens_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


def get_database_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(get_access_tokens_db),
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )


async def get_auth_manager(
    users_db: Annotated[
        "SQLAlchemyUserDatabase",
        Depends(get_users_db),
    ],
):
    yield AuthManager(users_db)


authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=BearerTransport(
        tokenUrl=settings.api.bearer_token_url,
    ),
    get_strategy=get_database_strategy,
)
