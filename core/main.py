import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():
    return {"message": "Hello World"}

items_list = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Doe"},
    {"id": 3, "name": "Jack"},
    {"id": 4, "name": "Kate"},
    {"id": 5, "name": "Mike"},
    {"id": 6, "name": "Alex"},
    {"id": 7, "name": "Bob"},
]

# all list of item
@app.get("/items")
async def read_items_list():
    return items_list

# specific item
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items_list:
        if item["id"] == item_id:
            return item
    return {"detail": "Item not found"}

# make item
@app.post("/items")
def create_item(name: str):
    name_new = {"id": random.randint(8, 10), "name": name}
    items_list.append(name_new)
    return items_list

# update whole item
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    for item in items_list:
        if item["id"] == item_id:
            item["name"] = name
            return item
    return {"detail": "Item not found"}

# remove item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items_list:
        if item["id"] == item_id:
            items_list.remove(item)
            return item
    return {"detail": "Item not found"}