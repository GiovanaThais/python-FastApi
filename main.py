from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel #pydantic valida dados e permite orm


app= FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get('/')
def read_root():
    """
    Leitura raiz. hello world da minha primeira api
    """
    return {"hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    Realiza atualização de registro de item
    """
    return {"item_name": item.name, "item_id": item_id}
