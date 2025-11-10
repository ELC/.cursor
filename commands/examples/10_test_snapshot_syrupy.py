import pytest
from syrupy.assertion import SnapshotAssertion
from api.serializers import serialize_user_profile


def test_serialize_user_profile_returns_expected_structure(
    user_with_valid_email: UserInput, snapshot: SnapshotAssertion
) -> None:
    result: dict[str, str | int] = serialize_user_profile(user_with_valid_email)

    assert result == snapshot


def test_serialize_multiple_users_returns_expected_structure(
    fake_database_with_users: FakeDatabaseRepository, snapshot: SnapshotAssertion
) -> None:
    all_users: list[UserData] = [
        user for user in fake_database_with_users.data.values()
    ]
    result: list[dict[str, str | int]] = [
        serialize_user_profile(user) for user in all_users
    ]

    assert result == snapshot

