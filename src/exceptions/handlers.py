from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.exceptions.already_exists import AssetAlreadyExists
from src.exceptions.auth import Unauthorized
from src.exceptions.input import QueryParamsCantAllBeNone
from src.exceptions.not_found import AssetNotFound


def already_exists_handler(request: Request, exc: AssetAlreadyExists) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=exc.message,
    )


def unauthorized_handler(request: Request, exc: Unauthorized) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"error": exc.message},
    )


def not_found_handler(request: Request, exc: AssetNotFound) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": exc.message},
    )


def empty_query_params_handler(request: Request, exc: QueryParamsCantAllBeNone) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": exc.message
        },
    )