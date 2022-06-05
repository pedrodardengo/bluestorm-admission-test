from src.pharmacies.controllers.pharmacy_controller import PHARMACIES_URL
from tests.acceptance.drivers.auth_driver import AuthDriver
from tests.acceptance.drivers.test_client import test_client_factory
from fastapi.testclient import TestClient


class PharmacyDriver(AuthDriver):
    def __init__(self):
        AuthDriver.__init__(self)
        self.__test_client: TestClient = test_client_factory()

    def get_pharmacies(self, token: str, **kwargs) -> dict:
        header = AuthDriver._generate_auth_header(token)
        return self.__test_client.get(
            PHARMACIES_URL, headers=header, params=kwargs
        ).json()
