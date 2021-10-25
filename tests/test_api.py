import os

from fastapi import status
from icecream import ic

from core.config import TEST_DATABASE_NAME
from main import app


class TestAPI:
    upload_file = "test_file.jpeg"

    def teardown_class(cls):
        os.remove(f"tests/{TEST_DATABASE_NAME}")

    def test_positive_create_user(self, test_client, some_user):
        response = test_client.post("/users/", json=some_user)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == "Max"
        assert data["email"] == "max@example.com"

    def test_negative_create_user(self, test_client, some_bad_user):
        response = test_client.post("/users/", json=some_bad_user)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        data = response.json()["detail"][0]
        assert data["loc"][1] == "password2"
        assert data["type"] == "value_error"
        assert data["msg"] == "password don't match"

    def test_login_user(self, test_client, some_user_login):
        response = test_client.post("/auth/", json=some_user_login)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert type(data['access_token']) == type(str())
        assert data["token_type"] == "Bearer"

    def test_upload_file(self, test_client, some_file):
        response = test_client.post("/frame/", files=some_file)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()[0]
        assert data["id"] == 1
        assert data["code"] == "/frame/"

    def test_upload_no_file(self, test_client):
        response = test_client.post("/frame/")
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        data = response.json()["detail"][0]
        assert data["loc"][1] == "up_file"
        assert data["type"] == "value_error.missing"
        assert data["msg"] == "field required"

    def test_get_list(self, test_client):
        response = test_client.get("/frame/")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()[0]
        assert data["id"] == 1
        assert data["code"] == "/frame/"

    def test_positive_delete_img(self, test_client):
        frame_id = 1
        response = test_client.delete(f"/frame/{frame_id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == True

    def test_negative_delete_img(self, test_client):
        frame_id = 100
        response = test_client.delete(f"/frame/{frame_id}")
        assert response.json()["status_code"] == status.HTTP_404_NOT_FOUND
        data = response.json()
        assert data["detail"] == "Not found frame"
        assert data["headers"] == None
