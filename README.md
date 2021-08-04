# Telstra Messaging

The SDK for the Telstra Messaging API enables you to send and receive messages
to Australian mobile numbers. For more information about this product, please
see here:
<https://dev.telstra.com/content/messaging-api>.

> :warning: **This SDK is experimental, everything is subject to change**

## Installing

```bash
pip install telstra.messaging
```

## Getting Started

Set the `TELSTRA_CLIENT_ID` and `TELSTRA_CLIENT_SECRET` environment variables. These
are the `Client id` and `Client secret` you can find here:
<https://dev.telstra.com/user/me/apps>.

To send your first message:

```python
from telstra.messaging import message

message.send(to="+61412345678", body="Hello from Python Messaging SDK!")
```

To set the required environment variables if your application is in `app.py`:

```bash
TELSTRA_CLIENT_ID"<client id>" TELSTRA_CLIENT_SECRET="<client secret>" python app.py
```

## Authentication

Authentication through environment variables, a shared credentials file and through code are supported.

### Authentication using environment variables

Export the following two environment variables, replacing the values with your own credentials.

```shell
export TELSTRA_CLIENT_ID="<client id>"
export TELSTRA_CLIENT_SECRET="<client secret>"
```

### Authentication using shared credentials

Create a `~/.telstra/credentials` file in your home path with the following contents, replacing the values with your own credentials.

```markdown
[default]
TELSTRA_CLIENT_ID = <client id>
TELSTRA_CLIENT_SECRET = <client secret>
```

### Authentication using code

On top of the authentication through the `TELSTRA_CLIENT_ID` and
`TELSTRA_CLIENT_SECRET` environment variables
and a `~/.telstra/credentials` shared credentials
file, authentication through code is also supported.
For example:

```python
from telstra.messaging.utils.config import CONFIG

CONFIG.telstra_client_id = '<client id>'
CONFIG.telstra_client_secret = '<client secret>'
```

This should be done before any interactions requiring authentication, such as
sending a message.

## Free Trial

Telstra offers a free trial for the messaging API to help you evaluate whether
it meets your needs. There are some restrictions that apply compared to the
full API, including a maximum number of messages that can be sent and requiring the
registration of a limited number of destinations before a message can be sent to that
destination. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#tag/Free-Trial>.

### Registering Destinations

> :information_source: **Only required for the free trial**

Register destinations for the free trial. For more information, please see
here:
<https://dev.telstra.com/content/messaging-api#operation/freeTrialBnumRegister>.

The function `telstra.messaging.trial_numbers.register` can be used to register
destinations. It takes the following arguments:

- `phone_numbers`: A list of destinations, expected to be phone numbers of the
  form `+614XXXXXXXX` or `04XXXXXXXX`.

Raises `telstra.messaging.exceptions.TrialNumbersError` if anything goes wrong.

It returns the list of phone numbers that have been registered.

For example:

```python
from telstra.messaging import trial_numbers

phone_numbers = trial_numbers.register(phone_numbers=["+61412345678"])
print(phone_numbers)
```

### Retrieve Destinations

> :information_source: **Only required for the free trial**

Retrieve destinations for the free trial. For more information, please see
here:
<https://dev.telstra.com/content/messaging-api#operation/freeTrialBnumList>.

The function `telstra.messaging.trial_numbers.get` can be used to retrieve registered
destinations. It takes no arguments.

Raises `telstra.messaging.exceptions.TrialNumbersError` if anything goes wrong.

It returns the list of phone numbers that
have been registered.

For example:

```python
from telstra.messaging import trial_numbers

phone_numbers = trial_numbers.get()
print(phone_numbers)
```

## Numbers

Gives you a dedicated mobile number tied to an application which
enables you to receive replies from your customers. For more information,
please see here:
<https://dev.telstra.com/content/messaging-api#tag/Provisioning>.

### Create Numbers

Create a new number for a dedicated mobile number. For more information,
please see here:
<https://dev.telstra.com/content/messaging-api#operation/createSubscription>.

The function `telstra.messaging.numbers.create` can be used to create a
numbers. It takes the following arguments:

- `active_days` (optional): The number of days the number will be active,
  defaults to 30.
- `notify_url` (optional): A notification URL that will be POSTed to whenever a
  new message (i.e. a reply to a message sent) arrives at this destination
  address.

Raises `telstra.messaging.exceptions.NumbersError` if anything goes wrong.

It returns an object with the following properties:

- `destination_address`: The phone number that a message can be sent to.
- `active_days`: The number of days left on the number.

For example:

```python
from telstra.messaging import numbers

created_numbers = numbers.create()
print(created_numbers)
```

### Retrieve Number

Retrieve the current number. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/getSubscription>.

The function `telstra.messaging.numbers.get` can be used to get the current
number. It takes no arguments.

Raises `telstra.messaging.exceptions.NumbersError` if anything goes wrong.

It returns an object with the following
properties:

- `destination_address`: The phone number that a message can be sent to.
- `active_days`: The number of days left.

For example:

```python
from telstra.messaging import numbers

retrieved_numbers = numbers.get()
print(retrieved_numbers)
```

### Delete Number

Delete the current number. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/deleteSubscription>.

The function `telstra.messaging.numbers.delete` can be used to delete the current
number. It takes no arguments.

Raises `telstra.messaging.exceptions.NumbersError` if anything goes wrong.

It returns nothing.

```python
from telstra.messaging import numbers

numbers.delete()
```

## Message

Send and receive messages. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#tag/Messaging>.

### Send Message

Send a message to a mobile number. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/sendSms>.

The function `telstra.messaging.message.send` can be used to send a message. It takes the
following arguments:

- `to`: The destination address, expected to be a phone number of the form
  `+614XXXXXXXX` or `04XXXXXXXX`.
- `body`: The message to send.
- `from_` (optional): An alphanumeric value which will appear as the sender.
  Note that phone numbers are not supported amd the maximum length is 11
  characters. Certain well know senders will be blocked.
- `validity` (optional): How long the platform should attempt to deliver the
  message for (in minutes).
- `scheduled_delivery` (optional): How long the platform should wait before
  attempting to send the message (in minutes).
- `notify_url` (optional): Contains a URL that will be called once your message
  has been processed.
- `priority` (optional): Message will be placed ahead of all messages with a
  normal priority.
- `reply_request` (optional): If set to true, the reply message functionality
  will be implemented.
- `receipt_off` (optional): Whether Delivery Receipt will be sent back or not.
- `user_msg_ref` (optional): Optional field used by some clients for custom
  reporting.
- `attachments` (optional): Optional field used by some clients to send an mms.
  reporting.
- `subject` (optional): Optional field used by some clients when sending an mms.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns an object with the following properties:

- `to`: The destination mobile number.
- `delivery_status`: Whether the delivery has been completed.
- `message_id`: Unique identifier for the message.
- `message_status_url`: URL to retrieve the current delivery status.

For example:

```python
# Send an SMS
from telstra.messaging import message

message.send(to="+61412345678", body="Hello from Python Messaging SDK!")

# Send an MMS
message.send(
    to="+61412345678",
    subject="Hello from Python Messaging SDK!",
    reply_request=True,
    attachments=[
      message.Attachments(
        type="<content type eg: image/png>",
        filename="<optional filename eg: bus.png>",
        payload="<base64 encoded string>",
      )
    ],
)
```

### Get Message Status

Find out whether a message has been sent. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/getSmsStatus>.

The function `telstra.messaging.message.get_status` can be used to retrieve
the status of a message. It takes the following arguments:

- `message_id`:Unique identifier for the message.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns an object with the following properties:

- `to`: Where the message is delivered to.
- `delivery_status`: Whether the delivery has been completed.
- `received_timestamp`: When the message was received.
- `sent_timestamp`: When the message was sent.

For example:

```python
from telstra.messaging import message

sent_message = message.send(to="+61412345678", body="Hello from Python Messaging SDK!")
status = message.get_status(sent_message.message_id)
print(status)
```

### Retrieve Reply

Retrieve messages sent to the mobile number associated with the number. For
more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/retrieveSmsReplies>.

The function `telstra.messaging.message.get_next_unread_reply` can be used to retrieve
the next unread reply for your phone number. It takes the
following arguments:

- `message_type`: Accepts `sms` or `mms` or None, defaults to `sms`.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns `None` if there are no more replies or an object with the
following properties:

- `destination_address`: Where the message is delivered to.
- `sender_address`: Who the message is from.
- `status`: Whether the delivery has been completed.
- `message`: The body of the message.
- `message_id`: Unique identifier for the message.
- `sent_timestamp`: When the message was sent.

For example:

```python
from telstra.messaging import message

reply = message.get_next_unread_reply()
print(reply)
```

## Exceptions

All exceptions that can be raised derive from `MessagingBaseException`:

```python
from telstra.messaging.exceptions import MessagingBaseException
```
