from logging import Formatter
from gunicorn.glogging import Logger
from app.config import settings


class GunicornLoger(Logger):
    def setup(self, cfg):
        super().setup(cfg)

        self._set_handler(
            log=self.access_log,
            output=cfg.accesslog,
            fmt=Formatter(fmt=settings.logging.log_format),
        )
        self._set_handler(
            log=self.error_log,
            output=cfg.errorlog,
            fmt=Formatter(fmt=settings.logging.log_format),
        )
