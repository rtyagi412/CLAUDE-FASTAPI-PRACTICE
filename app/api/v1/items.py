from fastapi import APIRouter, HTTPException, Response

from app.models import Item, ItemCreate
from app.store import store

router = APIRouter()


@router.get("/items")
def list_items() -> list[Item]:
    return store.list_all()


@router.post("/items", status_code=201)
def create_item(body: ItemCreate) -> Item:
    return store.create(body.name)


@router.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    item = store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> Response:
    if not store.delete(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(status_code=204)


@router.delete("/items", status_code=204)
def delete_all_items() -> Response:
    store.clear()
    return Response(status_code=204)
