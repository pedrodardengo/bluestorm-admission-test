from functools import lru_cache
from typing import Optional

from fastapi import Depends

from src.exceptions.already_exists import UserAlreadyExists
from src.users.entities.user_entity import User
from src.users.repositories.user_repository_impl import user_repository_impl_factory
from src.users.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repo = user_repository

    def add_user(self, username: str, salted_hash: str) -> str:
        found_username = self.__user_repo.add_user(username, salted_hash)
        if found_username is None:
            raise UserAlreadyExists(username)
        return username

    def find_user_by_username(self, username: str) -> Optional[User]:
        return self.__user_repo.find(username)


@lru_cache
def user_service_factory(
    user_repository: UserRepository = Depends(user_repository_impl_factory),
) -> UserService:
    return UserService(user_repository)
