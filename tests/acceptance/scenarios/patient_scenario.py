import pytest as pytest

from tests.acceptance.driver import driver_factory
from tests.acceptance.dsl.patient_dsl import PatientDSL

driver = driver_factory()
patient_dsl = PatientDSL(driver)


@pytest.fixture(autouse=True)
def run_around_tests():
    # Before Each
    yield
    # After Each
    patient_dsl.reset_data_cache()


def test_should_return_unauthorized_if_tries_get_patient_without_valid_token() -> None:
    # Arrange
    patient_dsl.do_not_login_as_admin()

    # Act
    patient_dsl.get_patient_01()

    # Assert
    patient_dsl.assert_response_is_unauthorized()


def test_should_get_patient_when_logged_as_admin() -> None:
    # Arrange
    patient_dsl.login_as_admin()

    # Act
    patient_dsl.get_patient_01()

    # Assert
    patient_dsl.assert_response_is_patient_01_data()


def test_should_return_not_found_if_patient_dont_exists():
    # Arrange
    patient_dsl.login_as_admin()

    # Act
    patient_dsl.get_non_existent_patient()

    # Assert
    patient_dsl.assert_response_is_not_found()
