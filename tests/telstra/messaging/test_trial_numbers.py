"""Tests for bun."""

import functools
from unittest.mock import patch

import pytest

from telstra.messaging import trial_numbers, exceptions, oauth
from tests.mocs import get_free_port, start_mock_server


class TestTrialNumbers(object):
    @classmethod
    def setup_class(cls):
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

        mock_oauth_url = "http://localhost:{port}/v2/oauth/token".format(
            port=cls.mock_server_port
        )

        # Patch _URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict("telstra.messaging.oauth.__dict__", {"_URL": mock_oauth_url}):
            oauth.get_token()

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
    @pytest.mark.trial_numbers
    def test_register_invalid_param(self, phone_numbers, expected_contents):
        """
        GIVEN invalid parameters
        WHEN register is called with the parameters
        THEN TrialNumbersError is raised with the expected contents.
        """
        with pytest.raises(exceptions.TrialNumbersError) as exc:
            trial_numbers.register(phone_numbers=phone_numbers)

        for content in expected_contents:
            assert content in str(exc)

    @pytest.mark.trial_numbers
    def test_register(self):
        """
        GIVEN
        WHEN register is called
        THEN phone numbers are registered.
        """
        phone_numbers = ["+61412345678"]

        mock_trial_numbers_url = (
            "http://localhost:{port}/v2/messages/freetrial/bnum".format(
                port=self.mock_server_port
            )
        )

        # Patch _URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict(
            "telstra.messaging.trial_numbers.__dict__", {"_URL": mock_trial_numbers_url}
        ):
            mocked = trial_numbers.register(phone_numbers=phone_numbers)

        assert mocked is not None
        assert mocked == phone_numbers

    # @pytest.mark.parametrize(
    #     "func",
    #     [
    #         pytest.param(
    #             functools.partial(trial_numbers.register, phone_numbers=[]), id="register"
    #         ),
    #         pytest.param(trial_numbers.get, id="get"),
    #     ],
    # )
    # @pytest.mark.trial_numbers
    # def test_error_oauth(self, func, mocked_oauth_get_token_error):
    #     """
    #     GIVEN oauth get_token that raises an error and a function
    #     WHEN the function is called
    #     THEN TrialNumbersError is raised.
    #     """
    #     with pytest.raises(exceptions.TrialNumbersError) as exc:
    #         func()

    #     assert mocked_oauth_get_token_error in str(exc.value)

    # @pytest.mark.parametrize(
    #     "func",
    #     [
    #         pytest.param(
    #             functools.partial(trial_numbers.register, phone_numbers=[]), id="register"
    #         ),
    #         pytest.param(trial_numbers.get, id="get"),
    #     ],
    # )
    # @pytest.mark.trial_numbers
    # def test_error_http(
    #     self, mocked_request_urlopen_error, _mocked_oauth_get_token, func
    # ):
    #     """
    #     GIVEN urlopen that raises an error and function
    #     WHEN the function is called is called
    #     THEN TrialNumbersError is raised.
    #     """
    #     with pytest.raises(exceptions.TrialNumbersError) as exc:
    #         func()

    #     assert mocked_request_urlopen_error.message in str(exc.value)
    #     assert str(mocked_request_urlopen_error.code) in str(exc.value)

    @pytest.mark.xfail
    @pytest.mark.trial_numbers
    def test_get(self, _valid_credentials):
        """
        GIVEN
        WHEN get is called
        THEN phone numbers are returned.
        """
        returned_phone_numbers = trial_numbers.get()

        assert isinstance(returned_phone_numbers, list)
