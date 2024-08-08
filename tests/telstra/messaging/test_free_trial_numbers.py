"""Tests for free_trial_numbers."""

from unittest.mock import patch

import pytest

from mocks.mocs import get_free_port, start_mock_server
from telstra.messaging import exceptions, free_trial_numbers, oauth


class TestFreeTrialNumbers(object):
    """Test Class for trial_numbers."""

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
    def test_create_invalid_param(self, phone_numbers, expected_contents):
        """
        GIVEN invalid parameters
        WHEN create is called with the parameters
        THEN TrialNumbersError is raised with the expected contents.
        """
        with pytest.raises(exceptions.FreeTrialNumbersError) as exc:
            free_trial_numbers.create(phone_numbers=phone_numbers)

        for content in expected_contents:
            assert content in str(exc)

    @pytest.mark.trial_numbers
    def test_create(self):
        """
        GIVEN
        WHEN create is called
        THEN phone numbers are registered.
        """
        phone_numbers = ["+61412345678"]

        mock_trial_numbers_url = (
            "http://localhost:{port}/messaging/v3/free-trial-numbers".format(
                port=self.mock_server_port
            )
        )

        # Patch _URL so that the service uses the mock server URL
        # instead of the real URL.
        with patch.dict(
            "telstra.messaging.free_trial_numbers.__dict__",
            {"_URL": mock_trial_numbers_url},
        ):
            mocked = free_trial_numbers.create(phone_numbers=phone_numbers)

        assert mocked is not None
        assert mocked == phone_numbers

    @pytest.mark.trial_numbers
    def test_get(self, _valid_credentials):
        """
        GIVEN
        WHEN get is called
        THEN phone numbers are returned.
        """
        mock_trial_numbers_url = (
            "http://localhost:{port}/messaging/v3/free-trial-numbers".format(
                port=self.mock_server_port
            )
        )

        # Patch _URL so that the service uses the mock server URL
        # instead of the real URL.
        with patch.dict(
            "telstra.messaging.free_trial_numbers.__dict__",
            {"_URL": mock_trial_numbers_url},
        ):
            mocked_returned_phone_numbers = free_trial_numbers.get_all()

        assert isinstance(mocked_returned_phone_numbers, list)
