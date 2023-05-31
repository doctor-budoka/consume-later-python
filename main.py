import sqlite3
from typing import Dict, List
from fastapi import FastAPI
import ibis

from utils.data import MediaType, Item

i_con = ibis.sqlite.connect("data.db")
ibis.options.interactive = False
app = FastAPI()


@app.get("/")
def get():
    return {}


@app.post("/add/{media_type}/")
def add(media_type: MediaType, item: Item):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO {media_type.value}(name, platform, genre, url) VALUES(?, ?, ?, ?)", (item.name, item.platform, item.genre, item.url))
    con.commit()


@app.get("/get/{media_type}/{name}/")
def get(media_type: MediaType, name: str) -> Dict:
    table = i_con.table(media_type.value)
    res = table.filter(table.name == name)
    
    if res.count().execute() > 0:
        print(res.head(1).execute().iloc[0].to_dict())
        return res.head(1).execute().iloc[0].to_dict()
    else:
        return {}


@app.get("/list/{media_type}/")
def list(media_type: MediaType) -> List[Dict]:
    table = i_con.table(media_type.value)
    ans = table.head(100).execute()
    return ans.to_dict("records")
