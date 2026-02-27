from app.models import Item


class ItemStore:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._next_id: int = 1

    def create(self, name: str) -> Item:
        item = Item(id=self._next_id, name=name)
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def delete(self, item_id: int) -> bool:
        if item_id not in self._items:
            return False
        del self._items[item_id]
        return True

    def clear(self) -> None:
        self._items.clear()
        self._next_id = 1


store = ItemStore()
