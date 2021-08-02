"""Tests for the messaging API."""

from telstra.messaging import exceptions, message, numbers


def test_create_numbers():
    """
    GIVEN credentials in the environment
    WHEN create, get and delete are called
    THEN no errors are raised.
    """
    numbers.create()
    numbers.get()
    numbers.delete()


def test_send_message():
    """
    GIVEN credentials in the environment
    WHEN send is called
    THEN no errors are raised.
    """
    numbers_value = numbers.get()
    message.send(to=numbers_value.destination_address, body="Test")


def test_get_reply():
    """
    GIVEN credentials in the environment
    WHEN send and then get_next_unread_reply is called
    THEN no errors are raised.
    """
    numbers_value = numbers.get()
    message.send(to=numbers_value.destination_address, body="Test")
    message.get_next_unread_reply()


def test_get_status():
    """
    GIVEN credentials in the environment and a sent message
    WHEN get_status is called
    THEN no errors are raised.
    """
    numbers_value = numbers.get()
    sent_message = message.send(to=numbers_value.destination_address, body="Test")

    retries = 5
    for retry_counter in range(retries):
        try:
            message.get_status(sent_message.message_id)
        except exceptions.MessageError as exc:
            if retry_counter == retries - 1:
                raise exc
