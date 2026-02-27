import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.store import store

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_store():
    store.clear()
    yield


# v1/health
def test_v1_health_returns_200() -> None:
    assert client.get("/v1/health").status_code == 200


def test_v1_health_returns_ok_body() -> None:
    assert client.get("/v1/health").json() == {"status": "ok"}


# echo
def test_echo_reflects_message() -> None:
    response = client.post("/v1/echo", json={"message": "hello"})
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}


# items
def test_create_item_returns_201() -> None:
    assert client.post("/v1/items", json={"name": "widget"}).status_code == 201


def test_create_item_body() -> None:
    response = client.post("/v1/items", json={"name": "widget"})
    assert response.json() == {"id": 1, "name": "widget"}


def test_get_item_returns_created() -> None:
    client.post("/v1/items", json={"name": "widget"})
    response = client.get("/v1/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "widget"}


def test_get_item_not_found() -> None:
    response = client.get("/v1/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_delete_item_returns_204() -> None:
    client.post("/v1/items", json={"name": "widget"})
    assert client.delete("/v1/items/1").status_code == 204


def test_delete_item_removes_item() -> None:
    client.post("/v1/items", json={"name": "widget"})
    client.delete("/v1/items/1")
    assert client.get("/v1/items/1").status_code == 404


def test_delete_item_not_found() -> None:
    response = client.delete("/v1/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


# list items
def test_list_items_empty() -> None:
    response = client.get("/v1/items")
    assert response.status_code == 200
    assert response.json() == []


def test_list_items_returns_all() -> None:
    client.post("/v1/items", json={"name": "widget"})
    client.post("/v1/items", json={"name": "gadget"})
    response = client.get("/v1/items")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "widget"},
        {"id": 2, "name": "gadget"},
    ]


# delete all items
def test_delete_all_items_returns_204() -> None:
    response = client.delete("/v1/items")
    assert response.status_code == 204


def test_delete_all_items_clears_store() -> None:
    client.post("/v1/items", json={"name": "widget"})
    client.post("/v1/items", json={"name": "gadget"})
    client.delete("/v1/items")
    assert client.get("/v1/items").json() == []


def test_delete_all_items_on_empty_store() -> None:
    response = client.delete("/v1/items")
    assert response.status_code == 204
    assert client.get("/v1/items").json() == []


def test_delete_all_then_get_individual_returns_404() -> None:
    client.post("/v1/items", json={"name": "widget"})
    client.delete("/v1/items")
    assert client.get("/v1/items/1").status_code == 404
