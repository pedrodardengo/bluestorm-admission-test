from functools import lru_cache
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.config.database_conn import ENGINE
from src.tools.uuid_tools import generate_uuid
from src.users.entities.user_entity import User
from src.users.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    """
    This class makes use of the SQLModel ORM (a wrapper to SQLAlchemy ORM).
    It works for almost any SQL database (see SQLAlchemy supported databases).
    To use a different database just set a new database connection string in the environment settings.
    """

    def add_user(self, username: str, salted_hash: str) -> Optional[str]:
        with Session(ENGINE) as session:
            user = User(id=generate_uuid(), username=username, salted_hash=salted_hash)
            stored_user = self.find(user.username)
            if stored_user is not None:
                return None
            session.add(user)
            session.commit()
            session.refresh(user)
            return username

    def find(self, username: str) -> Optional[User]:
        with Session(ENGINE) as session:
            statement = select(User).where(User.username == username)
            return session.scalars(statement).one_or_none()


@lru_cache
def user_repository_impl_factory() -> UserRepositoryImpl:
    return UserRepositoryImpl()
