"""Tests for phone number helper."""

import pytest

from messaging.utils import phone_number


@pytest.mark.parametrize(
    "value, expected_result, expected_reason_contents",
    [
        pytest.param(None, False, [f'"{None}"', "string"], id="None"),
        pytest.param(True, False, [f'"{True}"', "string"], id="True"),
        pytest.param(
            "invalid",
            False,
            ['"invalid"', "phone number", "+614", "04", "8 digits"],
            id="invalid string not number",
        ),
        pytest.param(
            "+6141234567",
            False,
            ['"+6141234567"', "incorrect number of characters", "12", "11"],
            id="invalid string starts with +614 too short",
        ),
        pytest.param(
            "+614123456789",
            False,
            ['"+614123456789"', "incorrect number of characters", "12", "13"],
            id="invalid string starts with +614 too long",
        ),
        pytest.param(
            "041234567",
            False,
            ['"041234567"', "incorrect number of characters", "10", "9"],
            id="invalid string starts with 04 too short",
        ),
        pytest.param(
            "04123456789",
            False,
            ['"04123456789"', "incorrect number of characters", "10", "11"],
            id="invalid string starts with 04 too long",
        ),
        pytest.param(
            "+614a2345678",
            False,
            ['"+614a2345678"', "contains invalid characters"],
            id="invalid string +614 invalid character",
        ),
        pytest.param(
            "04a2345678",
            False,
            ['"04a2345678"', "contains invalid characters"],
            id="invalid string 04 invalid character",
        ),
        pytest.param("+61412345678", True, None, id="valid with +614"),
        pytest.param("0412345678", True, None, id="valid with 04"),
    ],
)
def test_check(value, expected_result, expected_reason_contents):
    """
    GIVEN phone number
    WHEN check is called with the phone number
    THEN the expected result and contents in the reason are returned.
    """
    returned_result = phone_number.check(value)

    assert returned_result.valid == expected_result
    if not expected_result:
        for content in expected_reason_contents:
            assert content in returned_result.reason
    else:
        assert returned_result.reason is None
