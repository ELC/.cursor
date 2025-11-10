from collections.abc import Generator
import os
import pytest


@pytest.fixture
def _setup_test_database() -> Generator[None, None, None]:
    database_path: str = "test.db"
    initialize_test_database(database_path)
    yield
    cleanup_test_database(database_path)


@pytest.fixture
def _mock_environment_variables() -> Generator[None, None, None]:
    original_env: dict[str, str] = os.environ.copy()
    os.environ["TEST_MODE"] = "true"
    os.environ["API_URL"] = "http://test.local"
    yield
    os.environ.clear()
    os.environ.update(original_env)

