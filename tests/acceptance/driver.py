from functools import lru_cache

from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from src.auth.controllers.auth_controller import AUTH_URL
from src.config.database_conn import db_engine_factory
from src.main import app
from src.patients.controllers.patient_controller import PATIENTS_URL
from src.pharmacies.controllers.pharmacy_controller import PHARMACIES_URL
from src.transactions.controllers.transaction_controller import TRANSACTIONS_URL


class Driver:

    __ADMIN = {"username": "admin", "password": "Aa!!1111"}
    __TOKEN_URL = AUTH_URL + "/token"

    def __init__(self):
        engine = create_engine("sqlite:///../../../backend_test.db")
        app.dependency_overrides[db_engine_factory] = lambda: engine
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
        url = PATIENTS_URL + "/" + patient_id
        return self.__test_client.get(url, headers=header).json()

    def get_pharmacy(self, pharmacy_id: str, token: str) -> dict:
        header = self.__generate_auth_header(token)
        url = PHARMACIES_URL + "/" + pharmacy_id
        return self.__test_client.get(url, headers=header).json()

    def get_pharmacies(self, token: str, **kwargs) -> dict:
        header = self.__generate_auth_header(token)
        return self.__test_client.get(
            PATIENTS_URL, headers=header, params=kwargs
        ).json()

    def get_transactions(self, token: str, **kwargs) -> dict:
        header = self.__generate_auth_header(token)
        return self.__test_client.get(
            TRANSACTIONS_URL, headers=header, params=kwargs
        ).json()


@lru_cache()
def driver_factory() -> Driver:
    return Driver()
