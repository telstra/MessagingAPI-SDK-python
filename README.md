# Telstra Messaging

The SDK for the Telstra messaging API which enables you to send and receive SMS
for Australian mobile numbers. For more information about this product, please
see here:
<https://dev.telstra.com/content/messaging-api>.

> :warning: **This SDK is experimental, everything is subject to change**

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

This should be done before any interactions requiring authentication, such as
sending a SMS.

## Free Trial

Telstra offers a free trial for the messaging API to help you evaluate whether
it meets your needs. There are some restrictions that apply compared to the
full API, including a maximum number of SMS that can be sent and requiring the
registration of a limited number of destinations before SMS can be sent to that
destination. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#tag/Free-Trial>.

### Registering Destinations

> :information_source: **Only required for the free trial**

Register destinations for the free trial. For more information, please see
here:
<https://dev.telstra.com/content/messaging-api#operation/freeTrialBnumRegister>.

The function `tls.messaging.bnum.register` can be used to register
destinations. It takes the following arguments:

- `phone_numbers`: A list of destinations, expected to be phone numbers of the
  form `+614XXXXXXXX` or `04XXXXXXXX`.

It returns the list of phone numbers that have been registered.

For example:

```python
from tls.messaging import bnum

phone_numbers = bnum.register(phone_numbers=["+61412345678"])
print(phone_numbers)
```

### Retrieve Destinations

> :information_source: **Only required for the free trial**

Retrieve destinations for the free trial. For more information, please see
here:
<https://dev.telstra.com/content/messaging-api#operation/freeTrialBnumList>.

The function `tls.messaging.bnum.get` can be used to retrieve registered
destinations. It takes no arguments. It returns the list of phone numbers that
have been registered.

For example:

```python
from tls.messaging import bnum

phone_numbers = bnum.get()
print(phone_numbers)
```

## Subscription

A subscription gives you a dedicated mobile number tied to an application which
enables you to receive replies from your customers. For more information,
please see here:
<https://dev.telstra.com/content/messaging-api#tag/Provisioning>.

### Create Subscription

Create a new subscription for a dedicated mobile number. For more information,
please see here:
<https://dev.telstra.com/content/messaging-api#operation/createSubscription>.

The function `tls.messaging.subscription.create` can be used to create a
subscription. It takes the following arguments:

- `active_days` (optional): The number of days the subscription will be active,
  defaults to 30.
- `notify_url` (optional): A notification URL that will be POSTed to whenever a
  new message (i.e. a reply to a message sent) arrives at this destination
  address.

It returns an object with the following properties:

- `destination_address`: The phone number that a message can be sent to.
- `active_days`: The number of days left on the subscription.

For example:

```python
from tls.messaging import subscription

created_subscription = subscription.create()
print(created_subscription)
```

### Get Subscription

Retrieve the current subscription. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/getSubscription>.

The function `tls.messaging.subscription.get` can be used to get the current
subscription. It takes no arguments. It returns an object with the following
properties:

- `destination_address`: The phone number that a message can be sent to.
- `active_days`: The number of days left on the subscription.

For example:

```python
from tls.messaging import subscription

retrieved_subscription = subscription.get()
print(retrieved_subscription)
```

### Delete Subscription

Delete the current subscription. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/deleteSubscription>.

The function `tls.messaging.subscription.delete` can be used to delete the current
subscription. It takes no arguments.

```python
from tls.messaging import subscription

subscription.delete()
```

## SMS

Send and receive SMS. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#tag/Messaging>.

### Send SMS

Send a SMS to a mobile number. For more information, please see here:
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
- `notify_url` (optional): Contains a URL that will be called once your message
  has been processed.
- `priority` (optional): Message will be placed ahead of all messages with a
  normal priority.
- `reply_request` (optional): If set to true, the reply message functionality
  will be implemented.
- `receipt_off` (optional): Whether Delivery Receipt will be sent back or not.
- `user_msg_ref` (optional): Optional field used by some clients for custom
  reporting.

It returns an object with the following properties:

- `to`: The destination mobile number.
- `delivery_status`: Whether the delivery has been completed.
- `message_id`: Unique identifier for the message.
- `message_status_url`: URL to retrieve the current delivery status.

For example:

```python
from tls.messaging import sms

sms.send(to="+61412345678", body="Hi")
```

### Get SMS Status

Find out whether a SMS has been sent. For more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/getSmsStatus>.

The function `tls.messaging.sms.get_status` can be used to retrieve
the status of a SMS. It takes the following arguments:

- `message_id`:Unique identifier for the message.

It returns an object with the following properties:

- `to`: Where the message is delivered to.
- `delivery_status`: Whether the delivery has been completed.
- `received_timestamp`: When the message was received.
- `sent_timestamp`: When the message was sent.

For example:

```python
from tls.messaging import sms

sent_sms = sms.send(to="+61412345678", body="Hi")
status = sms.get_status(sent_sms.message_id)
print(status)
```

### Retrieve Replies

Retrieve SMS sent to the mobile number associated with the subscription. For
more information, please see here:
<https://dev.telstra.com/content/messaging-api#operation/retrieveSmsReplies>.

The function `tls.messaging.sms.get_next_unread_reply` can be used to retrieve
the next unread reply for your phone number subscription. It takes no
arguments. It returns `None` if there are no more replies or an object with the
following properties:

- `destination_address`: Where the message is delivered to.
- `sender_address`: Who the message is from.
- `status`: Whether the delivery has been completed.
- `message`: The body of the message.
- `message_id`: Unique identifier for the message.
- `sent_timestamp`: When the message was sent.

For example:

```python
from tls.messaging import sms

reply = sms.get_next_unread_reply()
print(reply)
```
