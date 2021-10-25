import os

from fastapi import status
from fastapi.testclient import TestClient
from icecream import ic

from core.config import TEST_DATABASE_NAME
from main import app


class TestUM:
    client = TestClient(app)
    upload_file = "test_file.jpeg"

    def teardown_class(cls):
        os.remove(f"tests/{TEST_DATABASE_NAME}")

    def test_positive_create_user(self, some_user):
        response = self.client.post("/users/", json=some_user)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["name"] == "Max"
        assert response.json()["email"] == "max@example.com"

    def test_negative_create_user(self, some_bad_user):
        response = self.client.post("/users/", json=some_bad_user)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "password don't match"

    def test_login_user(self, some_user_login):
        response = self.client.post("/auth/", json=some_user_login)
        assert response.status_code == status.HTTP_200_OK

    def test_upload_file(self, some_file):
        response = self.client.post("/frame/", files=some_file)
        assert response.status_code == status.HTTP_200_OK

    def test_upload_no_file(self):
        response = self.client.post("/frame/")
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_get_list(self):
        response = self.client.get("/frame/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]["id"] == 1

    def test_positive_delete_img(self):
        frame_id = 1
        response = self.client.delete(f"/frame/{frame_id}")
        assert response.status_code == status.HTTP_200_OK

    def test_negative_delete_img(self):
        frame_id = 100
        response = self.client.delete(f"/frame/{frame_id}")
        assert response.json()["status_code"] == status.HTTP_404_NOT_FOUND
