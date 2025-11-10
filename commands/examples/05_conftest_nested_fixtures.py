from collections.abc import Generator
import pytest


@pytest.fixture
def database_connection() -> FakeDatabaseRepository:
    return FakeDatabaseRepository()


@pytest.fixture
def user_repository(database_connection: FakeDatabaseRepository) -> UserRepository:
    return UserRepository(database_connection)


@pytest.fixture
def authenticated_user(user_repository: UserRepository) -> UserData:
    user_data: dict[str, str] = {"username": "testuser", "password": "hashed_pw"}
    user_id: str = user_repository.create_user(user_data)
    return user_repository.get_user(user_id)


@pytest.fixture
def user_with_posts(
    authenticated_user: UserData, database_connection: FakeDatabaseRepository
) -> UserData:
    posts: list[dict[str, str | int]] = [
        {"title": "First Post", "author_id": authenticated_user["id"]},
        {"title": "Second Post", "author_id": authenticated_user["id"]},
    ]
    for post in posts:
        database_connection.save(f"post_{post['title']}", UserData(post))
    return authenticated_user

