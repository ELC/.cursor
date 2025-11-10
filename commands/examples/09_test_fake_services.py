import pytest
from api.notifications import send_welcome_email


def test_send_welcome_email_delivers_email_successfully(
    user_with_valid_email: UserInput,
    fake_email_service: FakeEmailService,
    expected_welcome_success: bool,
    expected_email_count_after_welcome: int,
) -> None:
    result: bool = send_welcome_email(
        user_with_valid_email, email_service=fake_email_service
    )

    assert result == expected_welcome_success
    assert len(fake_email_service.sent_emails) == expected_email_count_after_welcome
    assert fake_email_service.sent_emails[0].to == user_with_valid_email.email
    assert "Welcome" in fake_email_service.sent_emails[0].subject

