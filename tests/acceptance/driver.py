from functools import lru_cache

from fastapi.testclient import TestClient
from src.main import app


class Driver:

    __ADMIN = {"username": "admin", "password": "Aa!!1111"}
    __TOKEN_URL = "/auth/token"
    __PATIENT_URL = "/patients"
    __PHARMACY_URL = "/pharmacies"
    __TRANSACTION_URL = "/transactions"

    def __init__(self):
        self.__test_client: TestClient = TestClient(app)

    @staticmethod
    def __generate_auth_header(token: str) -> dict:
        return {"Authorization": f"Bearer {token}"}

    def get_admin_token(self) -> str:
        return (
            self.__test_client.post(self.__TOKEN_URL, data=self.__ADMIN)
            .json()
            .get("access_token")
        )

    def get_patient(self, patient_id: str, token: str) -> dict:
        header = self.__generate_auth_header(token)
        url = self.__PATIENT_URL + "/" + patient_id
        return self.__test_client.get(url, headers=header).json()

    def get_pharmacy(self, pharmacy_id: str, token: str) -> dict:
        header = self.__generate_auth_header(token)
        url = self.__PHARMACY_URL + "/" + pharmacy_id
        return self.__test_client.get(url, headers=header).json()

    def get_pharmacies(self, token: str, **kwargs) -> dict:
        header = self.__generate_auth_header(token)
        return self.__test_client.get(
            self.__PATIENT_URL, headers=header, params=kwargs
        ).json()

    def get_transactions(self, token: str, **kwargs) -> dict:
        header = self.__generate_auth_header(token)
        return self.__test_client.get(
            self.__TRANSACTION_URL, headers=header, params=kwargs
        ).json()


@lru_cache()
def driver_factory() -> Driver:
    return Driver()
