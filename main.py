from fastapi import FastAPI
import ibis

from utils.data import MediaType, Item

con = ibis.sqlite.connect("data.db")
app = FastAPI()


@app.get("/")
def get():
    return {}


@app.post("/{media_type}/")
def add(media_type: MediaType, item: Item):
    table = con.table(media_type.value)
    table.insert(item)


@app.get("/{media_type}/{name}", response_model=Item)
def get(media_type: MediaType, name: str):
    table = con.table(media_type.value)
    res = table.filter(table.name == name)
    if res.count() > 0:
        return res[0]
    else:
        return {}


@app.post("/{media_type}/", response_model=Item)
def list(media_type: MediaType):
    table = con.table(media_type.value)
    if table.count() > 100:
        return table[:100]
    else:
        return table
