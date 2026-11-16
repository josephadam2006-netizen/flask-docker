import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_create_and_get_item(client):
    r = client.post("/api/items", json={"name": "widget"})
    assert r.status_code == 201
    item_id = r.get_json()["id"]
    r = client.get(f"/api/items/{item_id}")
    assert r.get_json()["name"] == "widget"


def test_create_requires_name(client):
    assert client.post("/api/items", json={}).status_code == 400
