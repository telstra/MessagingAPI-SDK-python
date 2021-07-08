"""Tests for bun."""

import functools

import pytest

from telstra.messaging import bnum, exceptions


@pytest.mark.parametrize(
    "phone_numbers, expected_contents",
    [
        pytest.param(
            None,
            ["phone_numbers", "received", f'"{None}"', "list", "string"],
            id="none",
        ),
        pytest.param(
            True,
            ["phone_numbers", "received", f'"{True}"', "list", "string"],
            id="True",
        ),
        pytest.param(
            [None],
            ["phone_numbers", "received", f'"{None}"'],
            id="list of single invalid",
        ),
        pytest.param(
            [None, None],
            ["phone_numbers", "received", f'"{None}"'],
            id="list of multiple invalid",
        ),
        pytest.param(
            [None, "+61412345678"],
            ["phone_numbers", "received", f'"{None}"'],
            id="list of first invalid",
        ),
        pytest.param(
            ["+61412345678", None],
            ["phone_numbers", "received", f'"{None}"'],
            id="list of second invalid",
        ),
    ],
)
@pytest.mark.bnum
def test_register_invalid_param(phone_numbers, expected_contents):
    """
    GIVEN invalid parameters
    WHEN register is called with the parameters
    THEN BnumError is raised with the expected contents.
    """
    with pytest.raises(exceptions.BnumError) as exc:
        bnum.register(phone_numbers=phone_numbers)

    for content in expected_contents:
        assert content in str(exc)


@pytest.mark.bnum
def test_register(_valid_credentials):
    """
    GIVEN
    WHEN register is called
    THEN phone numbers are registered.
    """
    phone_numbers = ["+61412345678"]

    returned_phone_numbers = bnum.register(phone_numbers=phone_numbers)

    assert returned_phone_numbers == phone_numbers


@pytest.mark.parametrize(
    "func",
    [
        pytest.param(functools.partial(bnum.register, phone_numbers=[]), id="register"),
        pytest.param(bnum.get, id="get"),
    ],
)
@pytest.mark.bnum
def test_error_oauth(func, mocked_oauth_get_token_error):
    """
    GIVEN oauth get_token that raises an error and a function
    WHEN the function is called
    THEN BnumError is raised.
    """
    with pytest.raises(exceptions.BnumError) as exc:
        func()

    assert mocked_oauth_get_token_error in str(exc.value)


@pytest.mark.parametrize(
    "func",
    [
        pytest.param(functools.partial(bnum.register, phone_numbers=[]), id="register"),
        pytest.param(bnum.get, id="get"),
    ],
)
@pytest.mark.bnum
def test_error_http(mocked_request_urlopen_error, _mocked_oauth_get_token, func):
    """
    GIVEN urlopen that raises an error and function
    WHEN the function is called is called
    THEN BnumError is raised.
    """
    with pytest.raises(exceptions.BnumError) as exc:
        func()

    assert mocked_request_urlopen_error.message in str(exc.value)
    assert str(mocked_request_urlopen_error.code) in str(exc.value)


@pytest.mark.xfail
@pytest.mark.bnum
def test_get(_valid_credentials):
    """
    GIVEN
    WHEN get is called
    THEN phone numbers are returned.
    """
    returned_phone_numbers = bnum.get()

    assert isinstance(returned_phone_numbers, list)
