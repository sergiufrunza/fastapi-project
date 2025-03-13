__all__ = (
    "main",
    "main_app",
)
from app.config import settings
from app.gunicorn import (
    Application,
    get_app_options,
)
from main import main_app


def main():
    app = Application(
        application=main_app,
        options=get_app_options(
            host=settings.gunicorn.host,
            port=settings.gunicorn.port,
            workers=settings.gunicorn.workers,
            timeout=settings.gunicorn.timeout,
            loglevel=settings.logging.log_level,
        ),
    )
    app.run()


if __name__ == "__main__":
    main()
