from src.exceptions.api_exception import APIException


class CouldNotValidateInput(APIException):
    def __init__(self, message: str) -> None:
        super().__init__(message, 400)


class QueryParamsCantAllBeNone(CouldNotValidateInput):
    def __init__(self, params: str | list[str]):
        message = f"The query params {params} can't all be None."
        super().__init__(message)


class CouldNotValidateDateString(CouldNotValidateInput):
    def __init__(self, date_string: str):
        message = (
            f"Could not validate date string: {date_string}."
            f"Incorrect data format, should be YYYY-MM-DD HH:MM:SS"
        )
        super().__init__(message)
