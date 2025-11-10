from collections.abc import Mapping, Sequence
from datetime import datetime
import pytest
from pydantic import BaseModel


class FakeEmailService:
    def __init__(self) -> None:
        self.sent_emails: list[EmailRecord] = []

    def send_email(self, to_address: str, subject: str, body: str) -> bool:
        email_record = EmailRecord(
            to=to_address,
            subject=subject,
            body=body,
            sent_at=datetime(2024, 1, 1, 0, 0, 0),
        )
        self.sent_emails.append(email_record)
        return True


class FakeDatabaseRepository:
    def __init__(self, initial_data: Mapping[str, UserData] | None = None) -> None:
        self.data: dict[str, UserData] = dict(initial_data) if initial_data else {}

    def get(self, key: str) -> UserData | None:
        return self.data.get(key)

    def save(self, key: str, value: UserData) -> bool:
        self.data[key] = value
        return True

    def delete(self, key: str) -> bool:
        if key in self.data:
            del self.data[key]
            return True
        return False


@pytest.fixture
def fake_email_service() -> FakeEmailService:
    return FakeEmailService()


@pytest.fixture
def fake_database_with_users() -> FakeDatabaseRepository:
    initial_data: dict[str, UserData] = {
        "user1": UserData(name="John", age=30, id=1),
        "user2": UserData(name="Jane", age=25, id=2),
    }
    return FakeDatabaseRepository(initial_data)


@pytest.fixture
def empty_fake_database() -> FakeDatabaseRepository:
    return FakeDatabaseRepository()


@pytest.fixture
def expected_user_john() -> UserData:
    return UserData(name="John", age=30, id=1)


@pytest.fixture
def expected_email_count_after_welcome() -> int:
    return 1


@pytest.fixture
def expected_welcome_success() -> bool:
    return True

