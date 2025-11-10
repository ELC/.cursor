from collections.abc import Sequence
import anyio
from utils.async_parser import async_fetch_and_validate, async_batch_validate


def test_async_fetch_and_validate_with_valid_data_returns_result(
    user_with_valid_email: UserInput, expected_validated_data: ValidatedData
) -> None:
    result: ValidatedData = anyio.run(
        async_fetch_and_validate, user_with_valid_email
    )

    assert result == expected_validated_data


def test_async_batch_validate_returns_all_results(
    list_of_users: Sequence[UserInput], expected_batch_results: Sequence[ValidatedData]
) -> None:
    result: list[ValidatedData] = anyio.run(async_batch_validate, list_of_users)

    assert result == expected_batch_results

