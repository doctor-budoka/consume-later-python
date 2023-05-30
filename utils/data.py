from enum import Enum
from pydantic import BaseModel


class MediaType(str, Enum):
    game = "game"
    movie = "movie"
    series = "series"
    album = "album"
    band = "band"


class Item(BaseModel):
    name: str
    platform: str | None = None
    genre: str | None = None
    url: str | None = None
