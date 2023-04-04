"""Utilities for the reports start and end dates."""

import datetime
import typing

from telstra.messaging import exceptions


def validate(
    *,
    start_date: typing.Optional[str],
    end_date: typing.Optional[str],
    exception: typing.Type[exceptions.MessagingBaseException],
) -> None:
    """Validate start and end date parameters for reports."""
    # Check if both start and end dates are provided
    if not isinstance(start_date, str):
        raise exception(
            'the value of "start_date" is not valid, '
            "expecting a 'YYYY-MM-YY' format date as string, "
            f'received "{start_date}"'
        )

    if not isinstance(end_date, str):
        raise exception(
            'the value of "end_date" is not valid, '
            "expecting a 'YYYY-MM-YY' format date as string, "
            f'received "{end_date}"'
        )

    # Convert start and end dates to datetime objects
    try:
        start_date_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    except Exception as exc:
        raise exception(
            f'The value of "start_date" is not valid, received "{start_date}"'
        ) from exc

    try:
        end_date_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except Exception as exc:
        raise exception(
            f'The value of "end_date" is not valid, received "{end_date}"'
        ) from exc

    # Check if both dates are in the past
    today = datetime.datetime.today().date()
    one_day = datetime.timedelta(days=1)
    tomorrow = today + one_day
    if start_date_datetime.date() > tomorrow or end_date_datetime.date() > tomorrow:
        raise exception(
            'the value of "start_date" or "end_date" is not valid, '
            "expecting a 'YYYY-MM-YY' format date in the past as string, "
            f'received "{start_date} - {end_date}"'
        )

    # Check if start_date is not ahead of end_date
    if start_date_datetime.date() > end_date_datetime.date():
        raise exception(
            'the value of "start_date" is not valid, '
            "expecting start_date to be older or same as end_date, "
            f'received "{start_date} - {end_date}"'
        )

    # Check if start date is not older than 3 months
    three_months_ago = today - datetime.timedelta(days=90)
    if start_date_datetime.date() < three_months_ago:
        raise exception(
            'the value of "start_date" is not valid, '
            "expecting a date not older than 3 months, "
            f'received "{start_date}"'
        )

    # # Check if end date is not more than 3 months from start date
    # three_months_from_start = start_date + datetime.timedelta(days=90)
    # if end_date.date() > three_months_from_start.date():
    #     raise exception(
    #         'the value of "end_date" is not valid, '
    #         "expecting a date less than 3 months from start_date, "
    #         f'received "{end_date}"'
    #     )
