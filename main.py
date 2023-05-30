from enum import Enum
from fastapi import FastAPI
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


app = FastAPI()

@app.post("/{media_type}/")
async def add(media_type: MediaType, item: Item):
    return {"message": "Hello World"}


@app.get("/{media_type}/{name}")
async def get(media_type: MediaType, name: str):
    return {"message": "Hello World"}
