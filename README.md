# Telstra Messaging

The SDK for the Telstra messaging API.

## Installing

```bash
pip install tls.messaging
```

## Getting Started

Set the `TLS_CLIENT_KEY` and `TLS_CLIENT_SECRET` environment variables. These
are the `Client key` and `Client secret` you can find here:
<https://dev.telstra.com/user/me/apps>.

To send your first SMS:

```python
from tls.messaging import sms

sms.send(to="+61412345678", body="Hi")
```

To set the required environment variables if your application is in `app.py`:

```bash
TLS_CLIENT_KEY="<client key>" TLS_CLIENT_SECRET="<client secret>" python app.py
```

## Authentication

On top of the authentication through the `TLS_CLIENT_KEY` and
`TLS_CLIENT_SECRET` environment variables, authentication through code is also
supported. For example:

```python
from tls.messaging.utils.config import CONFIG

CONFIG.tls_client_key = '<client key>'
CONFIG.tls_client_secret = '<client secret>'
```

## Subscription

A subscription gives you a dedicated mobile number tied to an application. For
more information, please see here:
<https://dev.telstra.com/content/messaging-api#tag/Provisioning>.

### Create Subscription

For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/createSubscription>.

The function `tls.messaging.subscription.create` can be used to create a
subscription. It takes the following arguments:

- `active_days`: The number of days the subscription will be active.

It returns an object with the following properties:

- `destination_address`: The phone number that a message can be sent to.
- `active_days`: The number of days left on the subscription.

### Get Subscription

For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/getSubscription>.

The function `tls.messaging.subscription.get` can be used to get the current
subscription. It takes no arguments. It returns an object with the following
properties:

- `destination_address`: The phone number that a message can be sent to.
- `active_days`: The number of days left on the subscription.

### Delete Subscription

For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/deleteSubscription>.

The function `tls.messaging.subscription.delete` can be used to delete the current
subscription. It takes no arguments.

## SMS

For more information, please see here:
<https://dev.telstra.com/content/messaging-api#tag/Messaging>.

### Send SMS

For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/sendSms>.

The function `tls.messaging.sms.send` can be used to send SMS. It takes the
following arguments:

- `to`: The destination address, expected to be a phone number of the form
  `+614XXXXXXXX` or `04XXXXXXXX`.
- `body`: The SMS to send.
- `from_` (optional): An alphanumeric value which will appear as the sender.
  Note that phone numbers are not supported amd the maximum length is 11
  characters. Certain well know senders will be blocked.
- `validity` (optional): How long the platform should attempt to deliver the
  message for (in minutes).
- `scheduled_delivery` (optional): How long the platform should wait before
  attempting to send the message (in minutes).

It returns an object with the following properties:

- `to`: The destination mobile number.
- `delivery_status`: Whether the delivery has been completed.
- `message_id`: Unique identifier for the message.
- `message_status_url`: URL to retrieve the current delivery status.

### Retrieve Replies

For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/retrieveSmsReplies>.

The function `tls.messaging.sms.get_next_unread_reply` can be used to retrieve
the next unread reply for your phone number subscription. It takes no
arguments. It returns an object with the following properties:

- `destination_address`: Where the message is delivered to.
- `sender_address`: Who the message is from.
- `status`: Whether the delivery has been completed.
- `message`: The body of the message.
- `message_id`: Unique identifier for the message.
- `sent_timestamp`: When the message was sent.
