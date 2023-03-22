"""Tests for numbers."""

from unittest.mock import patch

import pytest

from mocks.mocs import get_free_port, start_mock_server
from telstra.messaging.v3 import exceptions, oauth, virtual_number


class TestNumbers(object):
    """Test Class for numbers."""

    @classmethod
    def setup_class(cls):
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

        mock_oauth_url = f"http://localhost:{cls.mock_server_port}/v2/oauth/token"

        # Patch _URL so that the service uses the mock server
        # URL instead of the real URL.
        with patch.dict(
            "telstra.messaging.v3.oauth.__dict__", {"_URL": mock_oauth_url}
        ):
            oauth.get_token()

    CREATE_PARAM_TESTS = [
        pytest.param("tags", ["Python", "SDK"], "tags", ["Python", "SDK"], id="tags"),
        pytest.param(
            "reply_callback_url",
            "https://example.com",
            "replyCallbackUrl",
            "https://example.com",
            id="reply_callback_url",
        ),
    ]

    @pytest.mark.parametrize(
        "name, value, expected_name, expected_value", CREATE_PARAM_TESTS
    )
    @pytest.mark.numbers
    def test_create_param(self, name, value, expected_name, expected_value):
        """
        GIVEN parameter name and value
        WHEN create is called with the parameter
        THEN a virtual number is created with the
        expected parameter name and value.
        """

        mock_trial_numbers_url = (
            f"http://localhost:{self.mock_server_port}/messaging/v3/virtual-numbers"
        )

        # Patch _URL so that the service uses the mock server URL
        # instead of the real URL.
        with patch.dict(
            "telstra.messaging.v3.virtual_number.__dict__",
            {"_URL": mock_trial_numbers_url},
        ):
            mocked = virtual_number.assign(**{name: value})

        assert mocked is not None
        assert mocked.virtual_number == "0400000001"

    @pytest.mark.parametrize(
        "func",
        [
            pytest.param(virtual_number.assign, id="assign"),
        ],
    )
    @pytest.mark.numbers
    def test_assign_error_oauth(self, func, mocked_oauth_get_token_error):
        """
        GIVEN numbers function and oauth that raises an error
        WHEN function is called
        THEN VirtualNumbersError is raised.
        """
        with pytest.raises(exceptions.VirtualNumbersError) as exc:
            func()

        assert mocked_oauth_get_token_error in str(exc.value)

    @pytest.mark.parametrize(
        "func",
        [
            pytest.param(virtual_number.get, id="get"),
            pytest.param(virtual_number.delete, id="delete"),
        ],
    )
    @pytest.mark.numbers
    def test_error_oauth(self, func, mocked_oauth_get_token_error):
        """
        GIVEN numbers function and oauth that raises an error
        WHEN function is called
        THEN VirtualNumbersError is raised.
        """
        with pytest.raises(exceptions.VirtualNumbersError) as exc:
            func(virtual_number="0400000001")

        assert mocked_oauth_get_token_error in str(exc.value)

    @pytest.mark.parametrize(
        "func",
        [
            pytest.param(virtual_number.assign, id="assign"),
        ],
    )
    @pytest.mark.numbers
    def test_assign_error_http(self, func, mocked_request_urlopen_error):
        """
        GIVEN numbers function and urlopen that raises an error
        WHEN function is called
        THEN VirtualNumbersError is raised.
        """
        with pytest.raises(exceptions.VirtualNumbersError) as exc:
            func()

        assert mocked_request_urlopen_error.message in str(exc.value)
        assert str(mocked_request_urlopen_error.code) in str(exc.value)

    @pytest.mark.parametrize(
        "func",
        [
            pytest.param(virtual_number.get, id="get"),
            pytest.param(virtual_number.delete, id="delete"),
        ],
    )
    @pytest.mark.numbers
    def test_error_http(self, func, mocked_request_urlopen_error):
        """
        GIVEN numbers function and urlopen that raises an error
        WHEN function is called
        THEN VirtualNumbersError is raised.
        """
        with pytest.raises(exceptions.VirtualNumbersError) as exc:
            func(virtual_number="0400000001")

        assert mocked_request_urlopen_error.message in str(exc.value)
        assert str(mocked_request_urlopen_error.code) in str(exc.value)
