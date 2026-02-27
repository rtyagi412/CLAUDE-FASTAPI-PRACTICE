from fastapi import APIRouter, HTTPException

from app.models import Item, ItemCreate
from app.store import store

router = APIRouter()


@router.post("/items", status_code=201)
def create_item(body: ItemCreate) -> Item:
    return store.create(body.name)


@router.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    item = store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
