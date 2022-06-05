from src.exceptions.not_found import PatientNotFound
from tests.acceptance.driver import Driver
from tests.acceptance.dsl.auth_dsl import AuthDSL


class PatientDSL(AuthDSL):
    def __init__(self, driver: Driver) -> None:
        AuthDSL.__init__(self, driver)
        self.__patient_id = ""

    def reset_data_cache(self):
        self._token = ""
        self.__patient_id = ""
        self._response = {}

    def get_patient_01(self) -> None:
        self.__patient_id = "PATIENT0001"
        self._response = self._driver.get_patient(self.__patient_id, self._token)

    def assert_response_is_patient_01_data(self) -> None:
        assert self._response == {
            "last_name": "SILVA",
            "first_name": "JOANA",
            "birth_date": "1996-10-25",
            "id": "PATIENT0001",
        }

    def get_non_existent_patient(self) -> None:
        self.__patient_id = "NOT_A_PATIENT"
        self._response = self._driver.get_patient(self.__patient_id, self._token)

    def assert_response_is_not_found(self) -> None:
        assert self._response == {
            "error": PatientNotFound.generate_message(self.__patient_id)
        }
