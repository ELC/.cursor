from collections.abc import Sequence
import pytest
from utils.parser import calculate_total, validate_email


def test_calculate_total_with_valid_numbers_returns_sum(
    list_of_numbers_to_sum: Sequence[int], expected_sum_of_numbers: int
) -> None:
    result: int = calculate_total(list_of_numbers_to_sum)

    assert result == expected_sum_of_numbers


def test_calculate_total_with_empty_list_returns_zero(
    empty_list: Sequence[int], expected_sum_of_empty_list: int
) -> None:
    result: int = calculate_total(empty_list)

    assert result == expected_sum_of_empty_list


def test_validate_email_with_valid_format_returns_true(
    user_with_valid_email: UserInput, expected_valid_email_result: bool
) -> None:
    result: bool = validate_email(user_with_valid_email.email)

    assert result == expected_valid_email_result


def test_validate_email_with_invalid_format_returns_false(
    user_with_invalid_email: UserInvalidInput, expected_invalid_email_result: bool
) -> None:
    result: bool = validate_email(user_with_invalid_email.email)

    assert result == expected_invalid_email_result


def test_validate_email_with_missing_data_raises_value_error(
    empty_user_data: UserInput,
) -> None:
    with pytest.raises(ValueError, match="Email is required"):
        validate_email(empty_user_data.email)


def test_validate_email_with_none_raises_type_error() -> None:
    with pytest.raises(TypeError, match="Email must be a string"):
        validate_email(None)

