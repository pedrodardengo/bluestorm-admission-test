from src.exceptions.auth import CouldNotValidate
from tests.acceptance.drivers.auth_driver import AuthDriver


class AuthDSL:
    def __init__(self) -> None:
        self.__driver = AuthDriver()
        self._token = ""
        self._response = {any: any}

    def do_not_login_as_admin(self) -> None:
        self._token = "AFakeToken"

    def login_as_admin(self) -> None:
        self._token = self.__driver.get_admin_token()

    def assert_response_is_unauthorized(self) -> None:
        assert self._response == {"error": CouldNotValidate.MESSAGE}
