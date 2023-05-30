from fastapi import FastAPI
import ibis

from utils.data import MediaType, Item

con = ibis.sqlite.connect("data.db")
app = FastAPI()


@app.post("/{media_type}/")
async def add(media_type: MediaType, item: Item):
    table = con.table(media_type.value)
    table.a

    return {"message": "Hello World"}


@app.get("/{media_type}/{name}")
async def get(media_type: MediaType, name: str):
    return {"message": "Hello World"}
