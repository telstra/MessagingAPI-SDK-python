"""Tests for numbers."""

from unittest.mock import patch

import pytest

from telstra.messaging.v3 import exceptions, oauth, virtual_number
from tests.mocs import get_free_port, start_mock_server


class TestNumbers(object):
    """Test Class for numbers."""

    @classmethod
    def setup_class(cls):
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

        mock_oauth_url = "http://localhost:{port}/v2/oauth/token".format(
            port=cls.mock_server_port
        )

        # Patch _URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict(
            "telstra.messaging.v3.oauth.__dict__", {"_URL": mock_oauth_url}
        ):
            oauth.get_token()

    # @pytest.mark.parametrize(
    #     "kwargs, expected_contents",
    #     [
    #         pytest.param(
    #             {"tags": ["Python", "SDK"]},
    #             ["tags", "received", '["Python", "SDK"]', "list[str]"],
    #             id="tags string",
    #         ),
    #         pytest.param(
    #             {"reply_callback_url": True},
    #             ["reply_callback_url", "received", f'"{True}"', "string"],
    #             id="reply_callback_url not string",
    #         ),
    #         pytest.param(
    #             {"reply_callback_url": "example.com"},
    #             ["reply_callback_url", "received", '"example.com"', "https"],
    #             id="reply_callback_url not https",
    #         ),
    #     ],
    # )
    # @pytest.mark.numbers
    # def test_create_invalid_param(self, kwargs, expected_contents):
    #     """
    #     GIVEN invalid parameters
    #     WHEN create is called with the parameters
    #     THEN VirtualNumbersError is raised with the expected contents.
    #     """
    #     with pytest.raises(exceptions.VirtualNumbersError) as exc_info:
    #         virtual_number.assign(**kwargs)

    #     for content in expected_contents:
    #         assert content in str(exc_info.value)

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
    def test_create_param(
        self,
        name,
        value,
        expected_name,
        expected_value,
        monkeypatch,
        _mocked_oauth_get_token,
    ):
        """
        GIVEN parameter name and value
        WHEN create is called with the parameter
        THEN a virtual number is created with the expected parameter name and value.
        """

        mock_trial_numbers_url = (
            "http://localhost:{port}/messaging/v3/virtual-numbers".format(
                port=self.mock_server_port
            )
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

    # @pytest.mark.parametrize(
    #     "kwargs",
    #     [
    #         pytest.param({}, id="empty"),
    #         pytest.param(
    #             {"tags": ["V3"], "reply_callback_url": "https://example.com"},
    #             id="tags, reply_callback_url",
    #         ),
    #     ],
    # )
    # @pytest.mark.numbers
    # def test_create_get_delete(self, kwargs, _valid_credentials):
    #     """
    #     GIVEN valid credentials and kwargs
    #     WHEN create is called with the kwargs, get and delete is called
    #     THEN a numbers is provisioned, returned and deleted.
    #     """
    #     created_numbers = virtual_number.assign(**kwargs)

    #     assert created_numbers.virtual_number is "0400000001"
    #     assert created_numbers.reply_callback_url is not None
    #     assert created_numbers.tags is not None

    #     retrieved_numbers = virtual_number.get(virtual_number="0400000001")

    #     assert retrieved_numbers.reply_callback_url is not None
    #     assert retrieved_numbers.tags is not None
    #     assert retrieved_numbers.last_use is not None

    #     virtual_number.delete(virtual_number="0400000001")

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
    def test_assign_error_http(
        self, func, mocked_request_urlopen_error, _mocked_oauth_get_token
    ):
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
    def test_error_http(
        self, func, mocked_request_urlopen_error, _mocked_oauth_get_token
    ):
        """
        GIVEN numbers function and urlopen that raises an error
        WHEN function is called
        THEN VirtualNumbersError is raised.
        """
        with pytest.raises(exceptions.VirtualNumbersError) as exc:
            func(virtual_number="0400000001")

        assert mocked_request_urlopen_error.message in str(exc.value)
        assert str(mocked_request_urlopen_error.code) in str(exc.value)
