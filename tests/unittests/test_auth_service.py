import datetime
from unittest.mock import Mock

import pytest

from src.exceptions.auth import InvalidPassword, CouldNotValidate, TokenHasExpired
from src.exceptions.not_found import UserNotFound
from src.modules.auth.dto.token_dto import Token
from src.modules.auth.services.auth_service import AuthService


@pytest.fixture()
def settings_mock():
    return Mock()


@pytest.fixture()
def user_service_mock():
    return Mock()


@pytest.fixture()
def auth_service(user_service_mock, settings_mock):
    return AuthService(user_service_mock, settings_mock)


# save_user_in_repository -----------------------------------------------------


def test_should_call_add_user_and_get_salt(auth_service, user_service_mock) -> None:
    # Arrange
    user = Mock()
    user.username = "usernameOfUser"
    user.get_salted_hash.return_value = "salted_hash"

    # Act
    auth_service.save_user_in_repository(user)

    # Assert
    user.get_salted_hash.assert_called_once()
    user_service_mock.add_user.assert_called_once_with("usernameOfUser", "salted_hash")


# -----------------------------------------------------------------------------

# authenticate_user -----------------------------------------------------------


def test_should_raise_if_user_not_found(auth_service, user_service_mock) -> None:
    # Arrange
    user = Mock()
    user.username = "usernameOfUser"
    user.get_salted_hash.return_value = "salted_hash"
    user_service_mock.find_user_by_username.return_value = None

    # Act & Assert
    with pytest.raises(UserNotFound):
        auth_service.authenticate_user(user)
    user_service_mock.find_user_by_username.assert_called_once_with("usernameOfUser")


def test_should_raise_if_password_is_invalid(auth_service, user_service_mock) -> None:
    # Arrange
    user = Mock()
    user.username = "usernameOfUser"
    user.password = "password"
    user.get_salted_hash.return_value = "salted_hash"
    user_service_mock.find_user_by_username.return_value = user
    user.is_password_valid.return_value = False

    # Act & Assert
    with pytest.raises(InvalidPassword):
        auth_service.authenticate_user(user)
    user.is_password_valid.assert_called_once_with("password")


def test_should_return_username_of_user_if_authentication_succeeds(
    auth_service, user_service_mock
) -> None:
    # Arrange
    user = Mock()
    user.username = "usernameOfUser"
    user.password = "password"
    user.get_salted_hash.return_value = "salted_hash"
    user_service_mock.find_user_by_username.return_value = user
    user.is_password_valid.return_value = True

    # Act
    username = auth_service.authenticate_user(user)

    # Assert
    assert username == "usernameOfUser"


# -----------------------------------------------------------------------------

# create_access_token ---------------------------------------------------------


def test_should_return_token_given_username(auth_service, settings_mock) -> None:
    # Arrange
    username = "usernameOfUser"
    settings_mock.get_expiration_date.return_value = datetime.datetime.now()
    settings_mock.TOKEN_SECRET = "token_secret"
    # Act
    token = auth_service.create_access_token(username)

    # Assert
    assert isinstance(token, Token)
    assert token.access_token is not None
    assert token.token_type == "bearer"


# -----------------------------------------------------------------------------

# retrieve_user_from_token ----------------------------------------------------


def test_should_raise_if_token_is_invalid(
    auth_service, user_service_mock, settings_mock
) -> None:
    # Arrange
    token = "token"
    settings_mock.TOKEN_SECRET = "token_secret"
    user_service_mock.find_user_by_username.return_value = None

    # Act & Assert
    with pytest.raises(CouldNotValidate):
        auth_service.retrieve_user_from_token(token)


def test_should_raise_if_token_has_expired(
    auth_service, user_service_mock, settings_mock
) -> None:
    # Arrange
    username = "usernameOfUser"
    settings_mock.get_expiration_date.return_value = (
        datetime.datetime.now() - datetime.timedelta(hours=3)
    )
    settings_mock.TOKEN_SECRET = "token_secret"
    token = auth_service.create_access_token(username).access_token

    # Act & Assert
    with pytest.raises(TokenHasExpired):
        auth_service.retrieve_user_from_token(token)


def test_should_return_user_if_token_is_valid(
    auth_service, user_service_mock, settings_mock
) -> None:
    # Arrange
    user = Mock()
    user.username = "usernameOfUser"
    settings_mock.get_expiration_date.return_value = (
        datetime.datetime.now() + datetime.timedelta(hours=4)
    )
    settings_mock.TOKEN_SECRET = "token_secret"
    user_service_mock.find_user_by_username.return_value = user
    token = auth_service.create_access_token(user.username).access_token

    # Act
    user = auth_service.retrieve_user_from_token(token)

    # Assert
    assert user.username == "usernameOfUser"


# -----------------------------------------------------------------------------
