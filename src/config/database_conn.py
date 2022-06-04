from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

ENGINE = create_engine("sqlite:///../backend_test.db", )
Base = declarative_base()
