from functools import lru_cache
from fastapi.testclient import TestClient
from src.main import app


@lru_cache()
def client_factory() -> TestClient:

    # In Case you want to inject the database you might want to use a dependency override
    # databases = pathlib.Path(__file__).parent.parent.parent.parent
    # sqlite_db_path = (databases / f"backend_test.db").resolve()
    # engine = create_engine(f"sqlite:///{sqlite_db_path}")
    # app.dependency_overrides[db_engine_factory] = lambda: engine
    return TestClient(app)
