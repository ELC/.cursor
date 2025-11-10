from collections.abc import Sequence
import pytest
from pydantic import BaseModel


@pytest.fixture(
    params=[
        UserInput(email="user@example.com", name="John Doe"),
        UserInput(email="admin@example.com", name="Admin User"),
        UserInput(email="test@test.org", name="Test User"),
    ]
)
def user_with_valid_email(request: pytest.FixtureRequest) -> UserInput:
    return request.param


@pytest.fixture(
    params=[
        UserInvalidInput(email="invalid-email", name="Jane Doe"),
        UserInvalidInput(email="@no-local-part.com", name="Bad Email"),
        UserInvalidInput(email="missing-at-sign.com", name="Another Bad"),
    ]
)
def user_with_invalid_email(request: pytest.FixtureRequest) -> UserInvalidInput:
    return request.param


@pytest.fixture
def empty_user_data() -> UserInput:
    return UserInput(email="", name="")


@pytest.fixture(
    params=[
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [100],
    ]
)
def list_of_numbers_to_sum(request: pytest.FixtureRequest) -> list[int]:
    return request.param


@pytest.fixture
def empty_list() -> list[int]:
    return []


@pytest.fixture
def expected_sum_of_numbers(list_of_numbers_to_sum: Sequence[int]) -> int:
    return sum(list_of_numbers_to_sum)


@pytest.fixture
def expected_sum_of_empty_list() -> int:
    return 0


@pytest.fixture
def expected_valid_email_result() -> bool:
    return True


@pytest.fixture
def expected_invalid_email_result() -> bool:
    return False

