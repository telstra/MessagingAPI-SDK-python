"""Tests for the messaging API."""

import random

from telstra.messaging import free_trial_numbers, message, virtual_number
from telstra.messaging.exceptions import MessageError, VirtualNumbersError


def test_create_numbers():
    """
    GIVEN credentials in the environment
    WHEN create, get and delete are called
    THEN no errors are raised.
    """
    vn_response = None
    try:
        vn_response = virtual_number.assign()
        virtual_number.get(virtual_number=vn_response.virtual_number)
        virtual_number.delete(virtual_number=vn_response.virtual_number)
    except VirtualNumbersError as exception_:
        if "contact support to add more" not in str(exception_):
            raise exception_


def test_send_get_message():
    """
    GIVEN credentials in the environment
    WHEN send is called
    THEN no errors are raised.
    """

    try:

        virtual_number.assign()
        virtual_numbers = virtual_number.get_all()
        account_free_trial_numbers = free_trial_numbers.get_all()

        if len(virtual_numbers.virtual_numbers) > 0:
            vn = virtual_numbers.virtual_numbers[0].virtual_number
            if len(account_free_trial_numbers) > 0:
                free_trial_number = random.choice(account_free_trial_numbers)
                message_response = message.send(
                    to=free_trial_number,
                    from_=vn,
                    message_content="Prod Test",
                )
                message.get(message_id=message_response.message_id)
                virtual_number.delete(virtual_number=vn)
        else:
            if len(account_free_trial_numbers) > 0:
                free_trial_number = random.choice(account_free_trial_numbers)
                # Send the message to the random mobile number
                message_response = message.send(
                    to=free_trial_number,
                    from_=free_trial_number,
                    message_content="Prod Test",
                )

                message.get(message_id=message_response.message_id)
    except MessageError as exception_:
        if "upgrade to a paid" not in str(exception_):
            raise exception_
