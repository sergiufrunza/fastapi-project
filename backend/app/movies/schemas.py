import uuid

from pydantic import BaseModel
from datetime import date


class MovieRead(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    description: str
    year: int = 1900
    release_date: date
    release_date_cinero: date
    maturity_rating: str
    duration: int
    video_quality: str
    audio_quality: str
    price: int
    is_free: bool = False
    in_slider: bool = False
    renting_period: int
    vod: str
