"""Tests for oauth."""

import time
from unittest import mock

import pytest

from telstra.messaging.v3 import exceptions, oauth

TOKEN_TESTS = [
    pytest.param(1000000, "0", 1000000, True, id="instant expire no time change"),
    pytest.param(
        1000000,
        "1",
        1000000,
        False,
        id="1 second expire no time passed",
    ),
    pytest.param(
        1000000,
        "1",
        1000000.1,
        True,
        id="1 second expire less than 1 second passed",
    ),
    pytest.param(
        1000000,
        "1",
        1000001,
        True,
        id="1 second expire 1 second passed",
    ),
    pytest.param(
        1000000,
        "1",
        1000002,
        True,
        id="1 second expire more than 1 second passed",
    ),
    pytest.param(
        1000000,
        "1000",
        1000000,
        False,
        id="large expire no time passed",
    ),
    pytest.param(
        1000000,
        "1000",
        1000500,
        False,
        id="large expire less than expire time passed",
    ),
    pytest.param(
        1000000,
        "1000",
        1000999,
        False,
        id="large expire just less than expire time passed",
    ),
    pytest.param(
        1000000,
        "1000",
        1001000,
        True,
        id="large expire expire time passed",
    ),
    pytest.param(
        1000000,
        "1000",
        1001500,
        True,
        id="large expire more than expire time passed",
    ),
]


@pytest.mark.parametrize(
    "initial_time, expires_in, final_time, expected_expired", TOKEN_TESTS
)
def test_construct_token(
    monkeypatch, initial_time, expires_in, final_time, expected_expired
):
    """
    GIVEN mocked time
    WHEN a token is constructed
    THEN it is expired or not as expected.
    """

    mock_time = mock.MagicMock()
    mock_time.return_value = initial_time
    monkeypatch.setattr(time, "time", mock_time)
    access_token = "token 1"
    token_type = "type 1"

    token = oauth.TToken(
        access_token=access_token, token_type=token_type, expires_in=expires_in
    )

    mock_time.return_value = final_time

    assert token.expired == expected_expired
    assert token.authorization == f"Bearer {access_token}"


class TestGetToken:
    """Tests for _get_token."""

    # pylint: disable=protected-access

    # @staticmethod
    # def test_get_token_success(_valid_credentials):
    #     """
    #     GIVEN mocked environment that returns valid credentials
    #     WHEN _get_token is called
    #     THEN the token is returned.
    #     """
    #     token = oauth._get_token()

    #     assert not token.expired

    @staticmethod
    def test_get_token_error():
        """
        GIVEN environment with invalid credentials
        WHEN _get_token is called
        THEN CredentialError is raised.
        """
        with pytest.raises(exceptions.CredentialError) as exc:
            oauth._get_token()

        assert "Unauthorized" in str(exc)
