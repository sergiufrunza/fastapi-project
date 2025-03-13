__all__ = ("AdminAuth",)
from .authentication import AdminAuth
import importlib
import pkgutil
from sqladmin import Admin, ModelView
from pathlib import Path
import logging

log = logging.getLogger(__name__)


def register_admin_views(admin: Admin):
    package = "admin_panel"
    for _, module_name, _ in pkgutil.iter_modules([str(Path(__file__).parent)]):
        module = importlib.import_module(f"{package}.{module_name}")

        for obj_name in dir(module):
            obj = getattr(module, obj_name)
            if (
                isinstance(obj, type)
                and issubclass(obj, ModelView)
                and obj is not ModelView
            ):
                admin.add_view(obj)
                log.info("✅ Added ModelView: %r", {obj.__name__})
