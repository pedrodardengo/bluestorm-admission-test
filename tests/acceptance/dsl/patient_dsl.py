from src.exceptions.auth import CouldNotValidate
from src.exceptions.not_found import PatientNotFound
from tests.acceptance.driver import Driver


class PatientDSL:
    def __init__(self, driver: Driver) -> None:
        self.__driver = driver
        self.__token = ""
        self.__patient_id = ""
        self.__response = {any: any}

    def reset_data_cache(self):
        self.__token = ""
        self.__patient_id = ""
        self.__response = {}

    def do_not_login_as_admin(self) -> None:
        self.__token = "AFakeToken"

    def login_as_admin(self) -> None:
        self.__token = self.__driver.get_admin_token()

    def get_patient_01(self) -> None:
        self.__patient_id = "PATIENT0001"
        self.__response = self.__driver.get_patient(self.__patient_id, self.__token)

    def assert_response_is_unauthorized(self) -> None:
        assert self.__response == {"error": CouldNotValidate.MESSAGE}

    def assert_response_is_patient_01_data(self) -> None:
        assert self.__response == {
            "last_name": "SILVA",
            "first_name": "JOANA",
            "birth_date": "1996-10-25",
            "id": "PATIENT0001",
        }

    def get_non_existent_patient(self) -> None:
        self.__patient_id = "NOT_A_PATIENT"
        self.__response = self.__driver.get_patient(self.__patient_id, self.__token)

    def assert_response_is_not_found(self) -> None:
        assert self.__response == {
            "error": PatientNotFound.generate_message(self.__patient_id)
        }
