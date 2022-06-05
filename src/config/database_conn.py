from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

__engine = create_engine("sqlite:///../backend_test.db")
Base = declarative_base()


@lru_cache()
def db_engine_factory():
    return __engine
