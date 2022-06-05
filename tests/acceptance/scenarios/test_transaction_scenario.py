import pytest as pytest
from tests.acceptance.dsl.transaction_dsl import TransactionDSL


transaction_dsl = TransactionDSL()


@pytest.fixture(autouse=True)
def run_around_tests():
    # Before Each
    yield
    # After Each
    transaction_dsl.reset_data_cache()


def test_should_return_unauthorized_if_tries_get_transaction_without_valid_token() -> None:
    # Arrange
    transaction_dsl.do_not_login_as_admin()

    # Act
    transaction_dsl.get_transaction_01()

    # Assert
    transaction_dsl.assert_response_is_unauthorized()


def test_should_get_transaction_by_id_when_logged_as_admin() -> None:
    # Arrange
    transaction_dsl.login_as_admin()

    # Act
    transaction_dsl.get_transaction_01()

    # Assert
    transaction_dsl.assert_response_is_transaction_01_data()


def test_should_get_transaction_01_through_filtering() -> None:
    # Arrange
    transaction_dsl.login_as_admin()

    # Act
    transaction_dsl.get_transaction_01_through_filtering()

    # Assert
    transaction_dsl.assert_response_is_transaction_01_data()
