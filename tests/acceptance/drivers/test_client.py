from functools import lru_cache
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from src.config.database_conn import db_engine_factory
from src.main import app


@lru_cache()
def test_client_factory() -> TestClient:
    engine = create_engine("sqlite:///../../../backend_test.db")
    app.dependency_overrides[db_engine_factory] = lambda: engine
    return TestClient(app)
