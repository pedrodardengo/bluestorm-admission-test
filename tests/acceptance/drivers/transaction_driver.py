from src.transactions.controllers.transaction_controller import TRANSACTIONS_URL
from tests.acceptance.drivers.auth_driver import AuthDriver
from tests.acceptance.drivers.test_client import client_factory
from fastapi.testclient import TestClient


class TransactionDriver(AuthDriver):
    def __init__(self):
        AuthDriver.__init__(self)
        self.__test_client: TestClient = client_factory()

    def get_transactions(self, token: str, **kwargs) -> dict:
        header = AuthDriver._generate_auth_header(token)
        return self.__test_client.get(
            TRANSACTIONS_URL, headers=header, params=kwargs
        ).json()
