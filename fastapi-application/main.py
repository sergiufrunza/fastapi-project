import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn
from router import router as api_router
from core.config import settings
from core.db import db_helper
from sqladmin import Admin
from admin_panel import register_admin_views, AdminAuth

logging.basicConfig(
    force=settings.logging.log_format,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
    docs_url=settings.run.docs_url,
)
admin = Admin(
    main_app,
    db_helper.engine,
    authentication_backend=AdminAuth(settings.superuser.secret_key),
)
register_admin_views(admin)

main_app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
