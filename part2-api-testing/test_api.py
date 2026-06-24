import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user_by_id():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"]
    assert data["email"]
    assert "@" in data["email"]


def test_create_post():
    payload = {
        "title": "SDET API test",
        "body": "Creating a post using JSONPlaceholder.",
        "userId": 1,
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] is not None
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_get_unknown_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/999", timeout=10)

    assert response.status_code == 404
    assert response.json() == {}