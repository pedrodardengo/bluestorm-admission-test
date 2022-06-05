import pytest as pytest
from tests.acceptance.dsl.pharmacy_dsl import PharmacyDSL


pharmacy_dsl = PharmacyDSL()


@pytest.fixture(autouse=True)
def run_around_tests():
    # Before Each
    yield
    # After Each
    pharmacy_dsl.reset_data_cache()


def test_should_return_unauthorized_if_tries_get_pharmacy_without_valid_token() -> None:
    # Arrange
    pharmacy_dsl.do_not_login_as_admin()

    # Act
    pharmacy_dsl.get_pharmacy_01()

    # Assert
    pharmacy_dsl.assert_response_is_unauthorized()


def test_should_get_pharmacy_by_id_when_logged_as_admin() -> None:
    # Arrange
    pharmacy_dsl.login_as_admin()

    # Act
    pharmacy_dsl.get_pharmacy_01()

    # Assert
    pharmacy_dsl.assert_response_is_pharmacy_01_data()


def test_should_get_pharmacy_filtering_by_name_and_city() -> None:
    # Arrange
    pharmacy_dsl.login_as_admin()

    # Act
    pharmacy_dsl.get_pharmacy_01_by_filtering_by_city_and_name()

    # Assert
    pharmacy_dsl.assert_response_is_pharmacy_01_data()
