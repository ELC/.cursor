@pytest.fixture
def expected_validated_data() -> ValidatedData:
    return ValidatedData(email="user@example.com", status="validated")


@pytest.fixture
def expected_batch_results() -> list[ValidatedData]:
    return [
        ValidatedData(email="user@example.com", status="validated"),
        ValidatedData(email="admin@example.com", status="validated"),
    ]

