from fastapi.testclient import TestClient
from src.auth.controllers.auth_controller import AUTH_URL
from tests.acceptance.drivers.test_client import test_client_factory


class AuthDriver:

    __ADMIN = {"username": "admin", "password": "Aa!!1111"}
    __TOKEN_URL = AUTH_URL + "/token"

    def __init__(self):
        self.__test_client: TestClient = test_client_factory()

    @staticmethod
    def _generate_auth_header(token: str) -> dict:
        return {"Authorization": f"Bearer {token}"}

    def get_admin_token(self) -> str:
        return (
            self.__test_client.post(self.__TOKEN_URL, data=self.__ADMIN)
            .json()
            .get("access_token")
        )
