from src.patients.controllers.patient_controller import PATIENTS_URL
from tests.acceptance.drivers.auth_driver import AuthDriver
from tests.acceptance.drivers.test_client import test_client_factory
from fastapi.testclient import TestClient


class PatientDriver(AuthDriver):
    def __init__(self):
        AuthDriver.__init__(self)
        self.__test_client: TestClient = test_client_factory()

    def get_patient(self, patient_id: str, token: str) -> dict:
        header = AuthDriver._generate_auth_header(token)
        url = PATIENTS_URL + "/" + patient_id
        return self.__test_client.get(url, headers=header).json()
