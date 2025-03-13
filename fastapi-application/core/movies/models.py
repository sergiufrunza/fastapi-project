from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
)
from sqlalchemy import Date, String, Integer, event
from slugify import slugify

from typing import TYPE_CHECKING

from core.db.base import Base
from core.mixins import IdIntPkMixin
from datetime import date


class Movie(IdIntPkMixin, Base):
    name: Mapped[str] = mapped_column(String(255), unique=True)
    slug: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, default=""
    )
    description: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(default=1900)
    release_date: Mapped[date] = mapped_column(Date())
    release_date_cinero: Mapped[date] = mapped_column(Date())
    maturity_rating: Mapped[str] = mapped_column(String(10), default="PG-13")
    duration: Mapped[int] = mapped_column(default=0)
    video_quality: Mapped[str] = mapped_column(String(30), default="FULL HD")
    audio_quality: Mapped[str] = mapped_column(String(30), default="Dolby")
    price: Mapped[int] = mapped_column(default=35)
    is_free: Mapped[bool] = mapped_column(default=False)
    in_slider: Mapped[bool] = mapped_column(default=False)
    renting_period: Mapped[int] = mapped_column(default=2)
    vod: Mapped[str] = mapped_column(String, nullable=True)

    @property
    def upload_vod(self):
        return None


@event.listens_for(Movie, "before_insert")
@event.listens_for(Movie, "before_update")
def generate_slug(mapper, connection, target):
    target.slug = slugify(target.name)
