import random
from fastapi import FastAPI, status, HTTPException, Form, Body
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")

async def root():
    return JSONResponse(content={"message": "Hello World"}, status_code=status.HTTP_200_OK)

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
    raise HTTPException(status_code=404, detail="Item not found")

# make item
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(name: str = Body(embed=True)):
    name_new = {"id": random.randint(8, 10), "name": name}
    items_list.append(name_new)
    return items_list

# update whole item
@app.put("/items/{item_id}", status_code=status.HTTP_200_OK)
def update_item(item_id: int, name: str = Form()):
    for item in items_list:
        if item["id"] == item_id:
            item["name"] = name
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# remove item
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    for item in items_list:
        if item["id"] == item_id:
            items_list.remove(item)
            return item
    raise HTTPException(status_code=404, detail="Item not found")