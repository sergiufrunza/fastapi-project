from sqladmin import ModelView
from core.models import Movie
from wtforms import FileField
from wtforms.validators import Optional
from fastapi.requests import Request
from . import bunny


class UserAdmin(ModelView, model=Movie):
    column_list = [Movie.name]

    async def scaffold_form(self, rules=None):
        form_class = await super().scaffold_form(rules=rules)
        form_class.upload_vod = FileField("VOD File", validators=[Optional()])
        return form_class

    async def on_model_change(
        self, data: dict, model: Movie, is_created: bool, request: Request
    ):
        vod_file = data.pop("upload_vod", None)
        if not vod_file or not hasattr(vod_file, "filename"):
            return
        if getattr(vod_file, "size", 0) > 0:
            file_bytes = await vod_file.read()
            filename = vod_file.filename
            cdn_url = await bunny.upload_to_bunny(file_bytes, filename)
            data["vod"] = cdn_url
