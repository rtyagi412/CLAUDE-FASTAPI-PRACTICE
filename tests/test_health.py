from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_200() -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_ok_body() -> None:
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_v1_health_returns_200() -> None:
    response = client.get("/v1/health")
    assert response.status_code == 200


def test_v1_health_returns_ok_body() -> None:
    response = client.get("/v1/health")
    assert response.json() == {"status": "ok"}
