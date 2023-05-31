import requests
from utils.data import Item, MediaType


def add_data(media_type, item):
    result = requests.post(f"http://127.0.0.1:8000/add/{media_type}/", json=item.__dict__)
    print(result)


if __name__ == "__main__":
    new_item = Item(
        name="Star Wars Jedi: Survivor",
        platform="PS5",
        genre="action-adventure",
        url="https://en.wikipedia.org/wiki/Star_Wars_Jedi:_Survivor",
    )
    add_data("game", new_item)
