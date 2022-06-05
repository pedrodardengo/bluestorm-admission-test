from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.modules.auth.dto.token_dto import Token
from src.modules.auth.services.auth_service import AuthService, auth_service_factory
from src.tools.users.dto.incoming_user_dto import IncomingUserDTO
from src.tools.users.entities.user_entity import User

AUTH_URL = "/auth"

auth_router = APIRouter(
    prefix=AUTH_URL,
    tags=["Authentication"],
    dependencies=[Depends(auth_service_factory)],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_user_from_token(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(auth_service_factory),
) -> User:
    """
    Every end point that wants to be protected by a OAuth2 standard needs to depend on this function.
    It will make sure a user can be retrieved from token
    """
    return auth_service.retrieve_user_from_token(token)


@auth_router.post("/signup")
async def sign_up(
    user: IncomingUserDTO = Body(),
    auth_service: AuthService = Depends(auth_service_factory),
) -> None:
    """
    Signs up the user in the repositories, it delegates to the
    auth service the task of interacting with the repositories.
    """
    auth_service.save_user_in_repository(user)


@auth_router.post("/token", response_model=Token)
async def get_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(auth_service_factory),
) -> Token:
    """
    Retrieves a token given that a form data containing an existing username with correct password.
    It will return a token object.
    """
    user = IncomingUserDTO(username=form_data.username, password=form_data.password)
    username = auth_service.authenticate_user(user)
    return auth_service.create_access_token(username)
