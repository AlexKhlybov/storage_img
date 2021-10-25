import pytest

from core.security import create_access_token


@pytest.fixture()
def some_user():
    user = {"name": "Max", "email": "max@example.com", "password": "123456789", "password2": "123456789"}
    return user


@pytest.fixture()
def some_user_login():
    user = {
        "email": "max@example.com",
        "password": "123456789",
    }
    return user


@pytest.fixture()
def some_bad_user():
    user = {"name": "Max", "email": "max@example.com", "password": "123456789", "password2": "56789"}
    return user


@pytest.fixture()
def some_file():
    upload_file = {"up_file": ("filename", open(f"tests/test_file.jpeg", "rb"), "image/jpeg")}
    return upload_file
