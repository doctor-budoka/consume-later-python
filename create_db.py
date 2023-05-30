from pathlib import Path
from utils.data import MediaType, Item
from sqlite3 import connect

ROOT = Path(__file__).parent
DB = ROOT / "data.db"

def create_db():
    con = connect(DB)
    cur = con.cursor()

    for m_type in MediaType:
        cur.execute(f"CREATE TABLE {m_type.value}(name,platform,genre,url)")


if __name__ == "__main__":
    create_db()
