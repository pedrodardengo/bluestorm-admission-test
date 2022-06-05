import pathlib
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


__sqlite_db_path = (
    pathlib.Path(__file__).parent.parent.parent / f"backend_test.db"
).resolve()
__engine = create_engine(f"sqlite:///{__sqlite_db_path}")
Base = declarative_base()


@lru_cache()
def db_engine_factory():
    return __engine
