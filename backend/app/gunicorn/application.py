from fastapi import FastAPI
from gunicorn.app.base import BaseApplication

class Application(BaseApplication):
    def __init__(
            self,
            application: FastAPI,
            options: dict):
        self.options = options
        self.application = application
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application