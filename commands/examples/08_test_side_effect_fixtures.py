import pytest
from api.handlers.user import create_user, fetch_user


@pytest.mark.usefixtures("_setup_test_database")
def test_create_user_with_valid_data_saves_to_database(
    user_with_valid_email: UserInput,
) -> None:
    user_id: int = create_user(user_with_valid_email)

    assert user_id is not None
    assert isinstance(user_id, int)


@pytest.mark.usefixtures("_setup_test_database", "_mock_environment_variables")
def test_fetch_user_with_existing_id_returns_user_data(
    fake_database_with_users: FakeDatabaseRepository, expected_user_john: UserData
) -> None:
    result: UserData | None = fetch_user("user1", database=fake_database_with_users)

    assert result == expected_user_john

