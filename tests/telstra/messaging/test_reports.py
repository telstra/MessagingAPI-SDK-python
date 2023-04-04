"""Tests for free_trial_numbers."""

import datetime
import json
from unittest.mock import patch

import pytest

from mocks.mocs import get_free_port, start_mock_server
from telstra.messaging import exceptions, reports, oauth


class TestReports(object):
    """Test Class for reports."""

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

    end_date = datetime.datetime.today().date()
    ten_days = datetime.timedelta(days=10)
    start_date = end_date - ten_days
    expected_get_result = json.dumps(
        {
            "reports": [
                {
                    "reportId": "6940c774-4335-4d2b-b758-4ecb19412e85",
                    "reportStatus": "completed",
                    "reportType": "messages",
                    "reportExpiry": "2023-01-01",
                }
            ]
        }
    )
    expected_create_report_result = json.dumps(
        {
            "reportId": "6940c774-4335-4d2b-b758-4ecb19412e85",
            "reportCallbackUrl": "https://www.example.com",
            "reportStatus": "queued",
        }
    )

    CREATE_PARAM_TESTS = [
        pytest.param(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
            expected_create_report_result,
            id="valid",
        ),
    ]

    @pytest.mark.parametrize(
        "start_date, end_date, expected_contents",
        CREATE_PARAM_TESTS,
    )
    @pytest.mark.reports
    def test_create(self, start_date, end_date, expected_contents):
        """
        GIVEN valid parameters
        WHEN create is called with the parameters
        THEN created report info is returned with the expected contents.
        """
        mock_reports_url = (
            f"http://localhost:{self.mock_server_port}/messaging/v3/reports"
        )

        # Patch _URL so that the service uses the mock server URL
        # instead of the real URL.
        with patch.dict(
            "telstra.messaging.reports.__dict__",
            {"_URL": mock_reports_url},
        ):
            mocked = reports.create(start_date=start_date, end_date=end_date)

        response = json.loads(expected_contents)
        assert mocked is not None
        assert mocked.report_id == response["reportId"]
