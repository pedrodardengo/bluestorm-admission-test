from src.exceptions.not_found import PharmacyNotFound
from tests.acceptance.driver import Driver
from tests.acceptance.dsl.auth_dsl import AuthDSL


class PharmacyDSL(AuthDSL):
    def __init__(self, driver: Driver) -> None:
        AuthDSL.__init__(self, driver)
        self.__pharmacy_id = ""

    def reset_data_cache(self):
        self._token = ""
        self.__pharmacy_id = ""
        self._response = {}

    def get_pharmacy_01(self) -> None:
        self.__pharmacy_id = "PHARM0001"
        self._response = self._driver.get_pharmacies(
            self._token, pharmacy_id=self.__pharmacy_id
        )

    def assert_response_is_pharmacy_01_data(self) -> None:
        assert self._response == {
            "id": "PHARM0001",
            "name": "DROGA MAIS",
            "city": "RIBEIRAO PRETO",
        }

    def get_non_existent_pharmacy(self) -> None:
        self.__pharmacy_id = "NOT_A_PHARMACY"
        self._response = self._driver.get_pharmacies(
            self._token, pharmacy_id=self.__pharmacy_id
        )

    def assert_response_is_not_found(self) -> None:
        assert self._response == {
            "error": PharmacyNotFound.generate_message(self.__pharmacy_id)
        }

    def get_pharmacy_01_by_filtering_by_city_and_name(self) -> None:
        pharmacy_01_inside_list = self._driver.get_pharmacies(
            self._token, name="DROGA MAIS", city="RIBEIRAO PRETO"
        )
        self._response = pharmacy_01_inside_list[0]
