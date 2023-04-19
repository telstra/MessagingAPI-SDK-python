"""Tests for the messaging API."""

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
    virtual_numbers = virtual_number.get_all()
    account_free_trial_numbers = free_trial_numbers.get_all()
    try:
        if len(virtual_numbers.virtual_numbers) > 0:
            vn = virtual_numbers.virtual_numbers[0].virtual_number
            if vn not in account_free_trial_numbers:
                free_trial_numbers.create(phone_numbers=[vn])
            message_response = message.send(
                to=vn,
                from_="privateNumber",
                message_content="Prod Test",
            )
            message.get(message_id=message_response.message_id)
        else:
            vn_response = virtual_number.assign()
            vn = vn_response.virtual_number
            if vn_response.virtual_number not in account_free_trial_numbers:
                free_trial_numbers.create(phone_numbers=[vn])
            message_response = message.send(
                to=vn_response.virtual_number,
                from_="privateNumber",
                message_content="Prod Test",
            )
            message.get(message_id=message_response.message_id)
            virtual_number.delete(virtual_number=vn)
    except MessageError as exception_:
        if "upgrade to a paid" not in str(exception_):
            raise exception_
