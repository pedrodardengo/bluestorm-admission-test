class Unauthorized(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__()


class InvalidPassword(Unauthorized):
    def __init__(self) -> None:
        super().__init__("Password is invalid.")


class TokenHasExpired(Unauthorized):
    def __init__(self) -> None:
        super().__init__("The token has expired.")


class CouldNotValidate(Unauthorized):
    MESSAGE = "It was not possible to validate the token."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)
