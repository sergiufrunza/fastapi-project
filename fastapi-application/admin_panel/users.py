from sqladmin import ModelView
from core.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.email]
