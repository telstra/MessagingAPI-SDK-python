"""Used to work with Free Trial Numbers."""

import dataclasses
import json
import typing
from urllib import error, request

from . import exceptions, oauth
from .utils import callback_url as callback_url_util
from .utils import error_response as error_response_util
from .utils import reports_dates as reports_dates_util

_URL = "https://products.api.telstra.com/messaging/v3/reports"


@dataclasses.dataclass
class TReport:
    """
    A report.

    Attrs:
        report_id: UUID to fetch your report.
        report_status: The status (queued, completed, failed) of the report.
        report_type: the type of report generated.
        report_expiry: The expiry date of your report. After this date, you will be unable to download your report.
        report_url: The download link for generated report (CSV file).
        report_callback_url: The callbackUrl you want us to notify when your report is ready for download.

    """

    report_id: str
    report_status: str = ""
    report_type: str = ""
    report_expiry: str = ""
    report_url: str = ""
    report_callback_url: str = ""


@dataclasses.dataclass
class TReports:
    """
    List of reports.

    Attrs:
        reports: list of reports

    """

    reports: list[TReport]


def get_all() -> TReports:
    """
    Retrieve all reports recently generated for your account.

    Returns:
        A list of reports.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.ReportsError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    reports_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(reports_request) as response:
            reports: list[TReport] = []
            reports_response_dict = json.loads(response.read().decode())
            reports_list = reports_response_dict.get("reports", [])

            if reports_list is not None and len(reports_list) > 0:
                reports = [
                    TReport(
                        report_id=d.get("reportId"),
                        report_status=d.get("reportStatus"),
                        report_type=d.get("reportType"),
                        report_expiry=d.get("reportExpiry"),
                    )
                    for d in reports_list
                ]

            return TReports(
                reports=([] if reports is None else reports),
            )
    except error.HTTPError as exc:
        suggested_actions_string = ""
        try:
            error_response = json.loads(exc.read().decode())
            list_of_error_dicts = error_response.get("errors", [])
            suggested_actions_string = (
                error_response_util.get_suggeted_actions_list_str(
                    list_of_error_dicts=list_of_error_dicts, key="suggested_action"
                )
            )
        except Exception:
            raise exceptions.ReportsError(f"Could not retrieve reports: {exc}") from exc
        raise exceptions.ReportsError(
            f"Could not retrieve reports. {suggested_actions_string}"
        ) from exc


def get(report_id: str) -> TReport:
    """
    Retrieve the a report.

    Returns:
        A single report.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.ReportsError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    report_request = request.Request(
        f"{_URL}/{report_id}", headers=headers, method="GET"
    )
    try:
        with request.urlopen(report_request) as response:
            report_dict = json.loads(response.read().decode())
            return TReport(
                report_id=report_dict.get("reportId"),
                report_status=report_dict.get("reportStatus"),
                report_url=report_dict.get("reportUrl", ""),
            )
    except error.HTTPError as exc:
        suggested_actions_string = ""
        try:
            error_response = json.loads(exc.read().decode())
            list_of_error_dicts = error_response.get("errors", [])
            suggested_actions_string = (
                error_response_util.get_suggeted_actions_list_str(
                    list_of_error_dicts=list_of_error_dicts, key="suggested_action"
                )
            )
        except Exception:
            raise exceptions.ReportsError(f"Could not retrieve report: {exc}") from exc
        raise exceptions.ReportsError(
            f"Could not retrieve report. {suggested_actions_string}"
        ) from exc


def _validate_create_args(  # pylint: disable=too-many-arguments
    start_date: typing.Optional[str],
    end_date: typing.Optional[str],
    report_callback_url: typing.Optional[str],
    filter_: typing.Optional[str],
) -> None:
    """Validate the arguments for create report."""
    # Validate dates
    reports_dates_util.validate(
        start_date=start_date,
        end_date=end_date,
        exception=exceptions.ReportsError,
    )

    # Validate reports_callback_url
    callback_url_util.validate(
        name="report_callback_url",
        value=report_callback_url,
        exception=exceptions.ReportsError,
    )

    # Validate filter
    if filter_ is not None and not isinstance(filter_, str):
        raise exceptions.ReportsError(
            'The value of "filter" is not valid, expected a string, '
            f'received "{filter_}"'
        )


def create(
    start_date: typing.Optional[str],
    end_date: typing.Optional[str],
    report_callback_url: typing.Optional[str] = None,
    filter_: typing.Optional[str] = None,
) -> TReport:
    """
    Create a report.

    Raises ReportsError if anything goes wrong.

    Args:
        start_date: Start date (inclusive) of reporting period here.
        end_date: End date (inclusive) of reporting period here.
        report_callback_url: Url to notify when report is ready for download.
        filter_: Properties to filter the message report by

    """

    _validate_create_args(
        start_date=start_date,
        end_date=end_date,
        report_callback_url=report_callback_url,
        filter_=filter_,
    )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.ReportsError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    data: typing.Dict[str, typing.Any] = {
        "startDate": start_date,
        "endDate": end_date,
    }
    if report_callback_url is not None:
        data["reportCallbackUrl"] = report_callback_url
    if filter_ is not None:
        data["filter"] = filter_
    data_str = json.dumps(data).encode()

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
    numbers_request = request.Request(
        f"{_URL}/messages", data=data_str, headers=headers, method="POST"
    )
    try:
        with request.urlopen(numbers_request) as response:
            report_dict = json.loads(response.read().decode())
            return TReport(
                report_id=report_dict.get("reportId"),
                report_callback_url=report_dict.get("reportCallbackUrl"),
                report_status=report_dict.get("reportStatus"),
            )
    except error.HTTPError as exc:
        suggested_actions_string = ""
        try:
            error_response = json.loads(exc.read().decode())
            list_of_error_dicts = error_response.get("errors", [])
            suggested_actions_string = (
                error_response_util.get_suggeted_actions_list_str(
                    list_of_error_dicts=list_of_error_dicts, key="suggested_action"
                )
            )
        except Exception as inner_exc:
            raise exceptions.ReportsError(
                f"Could not create report: {inner_exc}"
            ) from inner_exc
        raise exceptions.ReportsError(
            f"Could not create report. {suggested_actions_string}"
        ) from exc
