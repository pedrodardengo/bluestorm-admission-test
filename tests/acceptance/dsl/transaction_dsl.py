from src.exceptions.not_found import TransactionNotFound
from tests.acceptance.driver import Driver
from tests.acceptance.dsl.auth_dsl import AuthDSL


class TransactionDSL(AuthDSL):
    def __init__(self, driver: Driver) -> None:
        AuthDSL.__init__(self, driver)
        self.__transaction_id = ""

    def reset_data_cache(self):
        self._token = ""
        self.__transaction_id = ""
        self._response = {}

    def get_transaction_01(self) -> None:
        self.__transaction_id = "TRAN0001"
        self._response = self._driver.get_transactions(
            self._token, transaction_id=self.__transaction_id
        )

    def assert_response_is_transaction_01_data(self) -> None:
        assert self._response == {
            "id": "TRAN0001",
            "amount": 3.5,
            "patient_id": "PATIENT0045",
            "pharmacy_id": "PHARM0008",
            "timestamp": "2020-02-05",
            "patient": {
                "last_name": "SALOMAO",
                "first_name": "CRISTIANO",
                "birth_date": "1993-09-30",
                "id": "PATIENT0045",
            },
            "pharmacy": {"id": "PHARM0008", "name": "DROGAO SUPER", "city": "CAMPINAS"},
        }

    def get_non_existent_transaction(self) -> None:
        self.__transaction_id = "NOT_A_TRANSACTION"
        self._response = self._driver.get_transactions(
            self._token, transaction_id=self.__transaction_id
        )

    def assert_response_is_not_found(self) -> None:
        assert self._response == {
            "error": TransactionNotFound.generate_message(self.__transaction_id)
        }

    def get_transaction_01_through_filtering(self) -> None:
        transaction_01_inside_list = self._driver.get_transactions(
            self._token,
            pharmacy_id="PHARM0008",
            less_than=8,
            after_date="2020-01-01 00:00:00",
            before_date="2020-03-01 00:00:00",
        )
        self._response = transaction_01_inside_list[0]
