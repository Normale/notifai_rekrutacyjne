import pytest
from main import app
from fastapi.testclient import TestClient
from jose import jwt
from config import SECRET_KEY, AUTH_PAYLOAD


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibm90aWYuYWkifQ.2LqWUgLYilJGXye0AyN1PlHlIN_Jvw6iOGSmVv1buRg

token = jwt.encode(AUTH_PAYLOAD, key=SECRET_KEY)
headers = {"Authorization": f"Bearer {token}"}
client = TestClient(app)


def test_authentication_failure():
    response = client.post("/message/", json={"text": "123"})
    assert response.status_code == 403
    response = client.put(f"/message/1", json={"text": "123"})
    assert response.status_code == 403
    response = client.delete(f"/message/1")
    assert response.status_code == 403


def test_post_authentication():
    response = client.post("/message/", json={"text": "123"}, headers=headers)
    assert response.status_code == 200


def test_view_not_found():
    # The number is supposed to indicate non-existent resource
    # (I assume that there won't be that many messages during tests :)
    response = client.get(f"/message/{999999999999999}")
    assert response.status_code == 404


@pytest.mark.parametrize("text", ["ąęćńóśźżł", "normal message", "1",
                                  "Ihave160charactersIhave160charactersIhave160charactersIhave160"
                                  "charactersIhave160charactersIhave160charactersIhave160characters"
                                  "Ihave160charactersIhave160characte"])
def test_create_and_view(text: str):
    response = client.post("/message/", json={"text": text}, headers=headers)
    assert response.status_code == 200
    json = response.json()
    assert json["text"] == text
    nr = json["nr"]
    json = client.get(f"/message/{nr}").json()
    assert response.status_code == 200
    assert json["nr"] == nr
    assert json["text"] == text
    assert json["views"] == 1


def test_put_and_delete_authentication():
    response = client.post("/message/", json={"text": "123"}, headers=headers)
    nr = response.json()["nr"]
    response = client.put(
        f"/message/{nr}", json={"text": "123"}, headers=headers)
    assert response.status_code == 200
    response = client.delete(f"/message/{nr}", headers=headers)
    assert response.status_code == 200


def test_views_increment():
    nr = client.post(
        "/message/", json={"text": "123"}, headers=headers).json()["nr"]
    for i in range(1, 100):
        response = client.get(f"/message/{nr}")
        assert response.status_code == 200
        json = response.json()
        assert json["nr"] == nr
        assert json["text"] == "123"
        assert json["views"] == i


@pytest.mark.parametrize("edited", ["ąęćńóśźżł", "normal message", "1",
                                    "Ihave160charactersIhave160charactersIhave160charactersIhave160"
                                    "charactersIhave160charactersIhave160charactersIhave160characters"
                                    "Ihave160charactersIhave160characte"])
def test_message_edit(edited):
    response = client.post("/message/", json={"text": "text"}, headers=headers)
    nr = response.json()["nr"]
    response = client.put(
        f"/message/{nr}", json={"text": edited}, headers=headers)
    assert response.status_code == 200
    json = response.json()
    assert json["nr"] == nr
    assert json["text"] == edited
    assert json["views"] == 0


@pytest.mark.parametrize("text", ["",
                                  "Ihave161charactersIhave161charactersIhave161charactersIhave161"
                                  "charactersIhave161charactersIhave161charactersIhave161characters"
                                  "Ihave161charactersIhave161character"])
def test_length_constraint(text):
    response = client.post("/message/", json={"text": text}, headers=headers)
    assert response.status_code == 422


def test_delete():
    response = client.post("/message/", json={"text": "text"}, headers=headers)
    nr = response.json()["nr"]
    response = client.delete(f"/message/{nr}", headers=headers)
    assert response.status_code == 200
    json = response.json()
    assert json["detail"] == "Message successfully deleted"
    response = client.get(f"/message/{nr}")
    assert response.status_code == 404
