from datetime import datetime, timedelta
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """These are the environment variables loaded using Pydantic's BaseSettings"""

    TOKEN_SECRET: str = "sas"
    MINUTES_FOR_TOKEN_EXPIRATION: int = 60

    def get_expiration_date(self) -> datetime:
        """
        Returns the datetime of when the token will expire.
        :return: a datetime object
        """
        now = datetime.now()
        return now + timedelta(minutes=self.MINUTES_FOR_TOKEN_EXPIRATION)

    def __hash__(self):
        """Is only here in order to allow this class to be cached"""
        return hash(str(self))


@lru_cache
def settings_factory() -> Settings:
    return Settings()
