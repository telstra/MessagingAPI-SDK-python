# Telstra Messaging

The SDK for the Telstra Messaging API enables you to send and receive messages
to Australian mobile numbers. For more information about this product, please
see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverview?version=3.x>.

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

message.send(
  to="+61412345678",
  from_="privateNumber",
  message_content="Hello from Python Messaging SDK!"
  )
```

To set the required environment variables if your application is in `app.py`:

```bash
TELSTRA_CLIENT_ID"<client id>" TELSTRA_CLIENT_SECRET="<client secret>" python app.py
```

## Authentication

Authentication through environment variables, a shared credentials file
and through code are supported.

### Authentication using environment variables

Export the following two environment variables, replacing the values
with your own credentials.

```shell
export TELSTRA_CLIENT_ID="<client id>"
export TELSTRA_CLIENT_SECRET="<client secret>"
```

### Authentication using shared credentials

Create a `~/.telstra/credentials` file in your home path with the following contents,
replacing the values with your own credentials.

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
registration of a limited number of destinations before a message can be sent
to that destination. For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#FreeTrial>.

### Registering Free Trial Numbers

> :information_source: **Only required for the free trial**

Register numbers for the free trial. For more information, please see
here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#RegisteraFreeTrialNumber>.

The function `telstra.messaging.free_trial_numbers.create` can be used to register
destinations. It takes the following arguments:

- `phone_numbers`: A list of destinations, expected to be phone numbers
  of the form `04XXXXXXXX`.

Raises `telstra.messaging.exceptions.FreeTrialNumbersError` if anything goes wrong.

It returns the list of phone numbers that have been registered.

For example:

```python
# Register free trial numbers
from telstra.messaging import free_trial_numbers

phone_numbers = free_trial_numbers.create(phone_numbers=["+61412345678"])
print(phone_numbers)
```

### Fetch all Free Trial Numbers

> :information_source: **Only required for the free trial**

Fetch the Free Trial Number(s) currently assigned to your account. For more information,
please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#FetchyourFreeTrialNumbers>.

The function `telstra.messaging.free_trial_numbers.get_all`
can be used to retrieve registered destinations.
It takes no arguments.

Raises `telstra.messaging.exceptions.FreeTrialNumbersError` if anything goes wrong.

It returns the list of phone numbers that
have been registered.

For example:

```python
# Get all free trial numbers
from telstra.messaging import free_trial_numbers

phone_numbers = free_trial_numbers.get_all()
print(phone_numbers)
```

## Virtual Number

Gives you a dedicated mobile number tied to an application which
enables you to receive replies from your customers. For more information,
please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#VirtualNumbers>.

### Assign Virtual Number

When a recipient receives your message, you can choose whether they'll see a privateNumber,
Virtual Number or senderName (paid plans only) in the from field.
If you want to use a Virtual Number, use this function to assign one.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#AssignaVirtualNumber>.

The function `telstra.messaging.virtual_number.create` can be used to create a
numbers. It takes the following arguments:

- `reply_callback_url` (optional): The URL that replies to the
  Virtual Number will be posted to.
- `tags` (optional): Create your own tags and use them to fetch,
  sort and report on your Virtual Numbers through our other endpoints.
  You can assign up to 10 tags per number.

Raises `telstra.messaging.exceptions.VirtualNumbersError` if anything goes wrong.

It returns an object with the following properties:

- `virtual_number`: The Virtual Number assigned to your account.
- `last_use`: The last time the Virtual Number was used to send a message.
- `reply_callback_url`: The URL that replies to the
  Virtual Number will be posted to.
- `tags`: Any customisable tags assigned to the Virtual Number.

For example:

```python
# Assign a virtual number
from telstra.messaging import virtual_number

assigned_numbers = virtual_number.assign()
print(assigned_numbers)
```

### Fetch a Virtual Number

Fetch the tags, replyCallbackUrl and lastUse date for a Virtual Number.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#FetchaVirtualNumber>.

The function `telstra.messaging.virtual_number.get` can be used to get the current
number. It takes the following arguments:

- `virtual_number`: The Virtual Number assigned to your account.

Raises `telstra.messaging.exceptions.VirtualNumbersError` if anything goes wrong.

It returns an object with the following
properties:

- `virtual_number`: The Virtual Number assigned to your account.
- `last_use`: The last time the Virtual Number was used to send a message.
- `reply_callback_url`: The URL that replies to the
  Virtual Number will be posted to.
- `tags`: Any customisable tags assigned to the Virtual Number.

For example:

```python
# Get a virtual number
from telstra.messaging import virtual_number

retrieved_number = virtual_number.get(virtual_number="0400000001")
print(retrieved_number)
```

### Fetch all Virtual Numbers

Fetch all Virtual Numbers currently assigned to your account.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#FetchallVirtualNumbers>.

The function `telstra.messaging.virtual_number.get_all` can be used to
get the all virtual numbers associated to your account.
It takes the following arguments:

- `limit`: Tell us how many results you want us to return, up to a maximum of 50.
- `offset`: Use the offset to navigate between the response results.
  An offset of 0 will display the first page of results, and so on.
- `filter`: Filter your Virtual Numbers by tag or by number.

Raises `telstra.messaging.exceptions.VirtualNumbersError` if anything goes wrong.

It returns an object with the following
properties:

- `virtual_numbers`: A list of Virtual Numbers assigned to your account.
- `paging`: Paging information.

For example:

```python
# Get all virtual numbers
from telstra.messaging import virtual_number

retrieved_virtual_numbers = virtual_number.get_all()
print(retrieved_virtual_numbers)
```

### Update a Virtual Number

Update a virtual number attributes. For more information,
please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#UpdateaVirtualNumber>.

The function `telstra.messaging.virtual_number.update` can be used to update a
virtual number. It takes the following arguments:

- `virtual_number`: The Virtual Number assigned to your account.
- `reply_callback_url` (optional): The URL that replies to the
  Virtual Number will be posted to.
- `tags` (optional): Create your own tags and use them to fetch,
  sort and report on your Virtual Numbers through our other endpoints.
  You can assign up to 10 tags per number.

Raises `telstra.messaging.exceptions.VirtualNumbersError` if anything goes wrong.

It returns an object with the following properties:

- `virtual_number`: The Virtual Number assigned to your account.
- `last_use`: The last time the Virtual Number was used to send a message.
- `reply_callback_url`: The URL that replies to the
  Virtual Number will be posted to.
- `tags`: Any customisable tags assigned to the Virtual Number.

For example:

```python
# Update a virtual number
from telstra.messaging import virtual_number

updated_virtual_number = virtual_number.update(
  virtual_number="0400000001",
  tags=["sdk", "v3"]
  )
print(updated_virtual_number)
```

### Delete Virtual Number

Delete the a virtual number. For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#DeleteaVirtualNumber>.

The function `telstra.messaging.virtual_number.delete` can be used
to delete the current number. It takes the following arguments:

- `virtual_number`: The Virtual Number assigned to your account.

Raises `telstra.messaging.exceptions.VirtualNumbersError` if anything goes wrong.

It returns nothing.

```python
# Delete a virtual number
from telstra.messaging import virtual_number

virtual_number.delete(virtual_number="0400000001")
```

### Fetch all Recipient Optouts list

Fetch any mobile number(s) that have opted out of receiving messages
from a Virtual Number assigned to your account.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Fetchallrecipientoptoutslist>.

The function `telstra.messaging.virtual_number.get_optouts` can be used to
get the list of mobile numbers that have opted out of receiving messages
from a virtual number associated to your account.
It takes the following arguments:

- `virtual_number`: The Virtual Number assigned to your account.
- `limit`: Tell us how many results you want us to return, up to a maximum of 50.
- `offset`: Use the offset to navigate between the response results.
  An offset of 0 will display the first page of results, and so on.

Raises `telstra.messaging.exceptions.VirtualNumbersError` if anything goes wrong.

It returns an object with the following
properties:

- `recipient_optouts`: A list of recipient optouts.
- `paging`: Paging information.

For example:

```python
# Get all virtual numbers
from telstra.messaging import virtual_number

retrieved_optout_numbers = virtual_number.get_optouts(virtual_number="0400000001")
print(retrieved_optout_numbers)
```

## Message

Send and receive messages. For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Messages>.

### Send Message

Send a message to a mobile number, or to multiple mobile numbers.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#SendanSMSorMMS>.

The function `telstra.messaging.message.send` can be used to send a message.
It takes the following arguments:

- `to`: The destination address, expected to be a phone number of the form
  `+614XXXXXXXX` or `04XXXXXXXX`.
- `from_`: This will be either "privateNumber", one of your Virtual Numbers
  or your senderName.
- `message_content`(Either one of messageContent or multimedia is required).
  The content of the message.
- `multimedia` (Either one of messageContent or multimedia is required).
  MMS multimedia content.
- `retry_timeout` (optional): How many minutes you asked the server to
  keep trying to send the message.
- `schedule_send` (optional): The time (in Central Standard Time)
  the message is scheduled to send.
- `delivery_notification` (optional): If set to true, you will receive
  a notification to the statusCallbackUrl when your SMS or MMS
  is delivered (paid feature).
- `status_callback_url` (optional): The URL the API will call when the
  status of the message changes.
- `tags` (optional): Any customisable tags assigned to the message.

The dataclass `telstra.messaging.message.Multimedia`
can be used to build an mms payload.
It takes the following arguments:

- `type`: The content type of the attachment, for example `image/png`.
- `filename` (optional): Optional field, for example `image.png`.
- `payload`: The payload of an mms encoded as base64.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns an object with the following properties:

- `messageId`: Use this UUID with our other endpoints to fetch,
  update or delete the message.
- `status`: The status will be either queued, sent, delivered or expired.
- `to`: The recipient's mobile number(s).
- `from`: This will be either "privateNumber", one of your
  Virtual Numbers or your senderName.
- `message_content`: The content of the message.
- `multimedia`: The multimedia content of the message (MMS only).
- `retry_timeout`: How many minutes you asked the server to keep
  trying to send the message.
- `schedule_send`: The time (in Central Standard Time) a message
  is scheduled to send.
- `delivery_notification`: If set to true, you will receive a notification to the
  statusCallbackUrl when your SMS or MMS is delivered (paid feature).
- `status_callback_url`: The URL the API will call when the status of
  the message changes.
- `tags`: Any customisable tags assigned to the message.

For example:

```python
# Send an SMS
from telstra.messaging import message

message.send(
  to="+61412345678",
  from_="privateNumber",
  message_content="Hello from Python Messaging SDK!"
)

# Send an MMS
message.send(
    to="+61412345678",
    from_="privateNumber",
    multimedia=[
        message.Multimedia(
            type="image/jpeg",
            fileName="myFile.jpeg",
            payload="iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
        )
    ],
)
```

### Get a Message

Use the messageId to fetch a message that's been sent from/to
your account within the last 30 days.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Fetchamessage>.

The function `telstra.messaging.message.get` can be used to retrieve
the a message. It takes the following arguments:

- `message_id`:Unique identifier for the message.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns an object with the following properties:

- `message_id`: Use this UUID with our other endpoints to fetch,
  update or delete the message.
- `status`: The status will be either queued, sent, delivered or expired.
- `create_timestamp`: The time you submitted the message to
  the queue for sending.
- `sent_timestamp`: The time the message was sent from the server.
- `received_timestamp`: The time the message was received by the
  recipient's device.
- `to`: The recipient's mobile number(s).
- `from`: This will be either "privateNumber", one of your
  Virtual Numbers or your senderName.
- `message_content`: The content of the message.
- `multimedia`: The multimedia content of the message (MMS only).
- `direction`: Direction of the message (outgoing or incoming).
- `retry_timeout`: How many minutes you asked the server to keep
  trying to send the message.
- `schedule_send`: The time (in Central Standard Time) the message is
  scheduled to send.
- `delivery_notification`: If set to true, you will receive a notification
  to the statusCallbackUrl when your SMS or MMS is delivered (paid feature).
- `status_callback_url`: The URL the API will call when the status of
  the message changes.
- `queue_priority`: The priority assigned to the message.
- `tags`: Any customisable tags assigned to the message.

For example:

```python
# Get a message
from telstra.messaging import message

sent_message = message.send(
  to="+61412345678",
  from_="privateNumber",
  message_content="Hello from Python Messaging SDK!"
  )
message = message.get(message_id = sent_message.message_id)
print(message)
```

### Get all Messages

Fetch messages that have been sent from/to your account in the last 30 days.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Fetchallsent/receivedmessages>.

The function `telstra.messaging.message.get_all` can be used to fetch
all messages. It takes the
following arguments:

- `limit`: Tell us how many results you want us to return, up to a maximum of 50.
- `offset`: Use the offset to navigate between the response results.
  An offset of 0 will display the first page of results, and so on.
- `filter`: Filter your Virtual Numbers by tag or by number.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns `None` if there are no more replies or an object with the
following properties:

- `messages`: List of all messages.
- `paging`: Paging information.

For example:

```python
# Get all messages
from telstra.messaging import message

reply = message.get_all(limit=5,offset=0,filter="Python,SDK")
print(reply)
```

### Update a Message

Update a message that's scheduled for sending, you can change any of
the below parameters, as long as the message hasn't been sent yet.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Updateamessage>.

The function `telstra.messaging.message.update` can be used to update a message.
It takes the following arguments:

- `to`: The destination address, expected to be a phone number of the form
  `+614XXXXXXXX` or `04XXXXXXXX`.
- `from_`: This will be either "privateNumber", one of your
  Virtual Numbers or your senderName.
- `message_content`The content of the message.
  Either one of messageContent or multimedia is required.
- `multimedia` MMS multimedia content.
- `retry_timeout` (optional): How many minutes you asked the server to
  keep trying to send the message.
- `schedule_send` (optional): The time (in Central Standard Time) the
  message is scheduled to send.
- `delivery_notification` (optional): If set to true, you will receive a
  notification to the statusCallbackUrl when your SMS or MMS is delivered (paid feature).
- `status_callback_url` (optional): The URL the API will call when
  the status of the message changes.
- `tags` (optional): Any customisable tags assigned to the message.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

The dataclass `telstra.messaging.message.Multimedia` can be used to build
a mms payload. It takes the following arguments:

- `type`: The content type of the attachment, for example `image/png`.
- `filename` (optional): Optional field, for example `image.png`.
- `payload`: The payload of an mms encoded as base64.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns an object with the following properties:

- `messageId`: Use this UUID with our other endpoints to fetch,
  update or delete the message.
- `status`: The status will be either queued, sent, delivered or expired.
- `to`: The recipient's mobile number(s).
- `from`: This will be either "privateNumber", one of your
  Virtual Numbers or your senderName.
- `message_content`: The content of the message.
- `multimedia`: The multimedia content of the message (MMS only).
- `retry_timeout`: How many minutes you asked the server to keep trying
  to send the message.
- `schedule_send`: The time (in Central Standard Time) the message
  is scheduled to send.
- `delivery_notification`: If set to true, you will receive a notification to the
  statusCallbackUrl when your SMS or MMS is delivered (paid feature).
- `status_callback_url`: The URL the API will call when the
  status of the message changes.
- `tags`: Any customisable tags assigned to the message.

For example:

```python
# Update a message
from telstra.messaging import message

message.update(
  message_id="8540d774-4863-4d2b-b788-4ecb19412e85",
  to="+61412345678",
  from_="privateNumber",
  message_content="Hello from Python Messaging SDK!"
  )
```

### Update Message Tags

Update message tags, you can update them even after your message has been delivered.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Updatemessagetags>.

The function `telstra.messaging.message.update_tags` can be used to
update message tags. It takes the following arguments:

- `message_id`:Unique identifier for the message.
- `tags` (optional): Any customisable tags assigned to the message.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns nothing.

For example:

```python
# Update message tags
from telstra.messaging import message

message.update_tags(message_id="8540d774-4863-4d2b-b788-4ecb19412e85", tags=["Python","V3"])
```

### Delete a Message

Delete a scheduled message, but hasn't yet sent.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Deleteamessage>.

The function `telstra.messaging.message.delete` can be used to delete a message.
It takes the following arguments:

- `message_id`: Unique identifier for the message.

Raises `telstra.messaging.exceptions.MessageError` if anything goes wrong.

It returns nothing.

For example:

```python
# Delete a message
from telstra.messaging import message

message.delete(message_id="8540d774-4863-4d2b-b788-4ecb19412e85")
```

## Reports

Create and fetch reports. For more information, please see here:
<https://dev.telstra.com/content/messaging-api-v3#tag/reports>.

### Request a Report

Request a CSV report of messages (both incoming and outgoing)
that have been sent to/from your account within the last three months.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Submitarequestforamessagesreport>.

The function `telstra.messaging.reports.create` can be used to create a report.
It takes the following arguments:

- `start_date`: Set the time period you want to generate a
  report for by typing the start date (inclusive) here. Note that we only
  retain data for three months, so please ensure your startDate is not more
  than three months old. Use ISO format(yyyy-mm-dd), e.g. "2019-08-24".
- `end_date`: Type the end date (inclusive) of your reporting period here.
  Your endDate must be a date in the past, and less than three months from your startDate.
  Use ISO format(yyyy-mm-dd), e.g. "2019-08-24".
- `report_callback_url`: The callbackUrl where notification
  is sent when report is ready for download.
- `filter_`: Filter report messages by -
  tag - use one of the tags assigned to your message(s)
  number - either the Virtual Number used to send the message,
  or the Recipient Number the message was sent to.

Raises `telstra.messaging.exceptions.ReportsError` if anything goes wrong.

It returns an object with the following properties:

- `report_id`: Use this UUID with our other endpoints to fetch the report.
- `report_callback_url`: If you provided a reportCallbackUrl in your request,
  it will be returned here.
- `report_status`: The status of the report. It will be either:
  - queued – the report is in the queue for generation.
  - completed – the report is ready for download.
  - failed – the report failed to generate, please try again.

For example:

```python
# Create a report
from telstra.messaging import reports

reports_create_response = reports.create(
        start_date="2023-03-15", end_date="2023-03-30", filter_="0412345678"
    )
```

### Fetch a specific report

Use the report_id to fetch a download link for a report generated.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#FetchaReport>.

The function `telstra.messaging.reports.get` can be used to retrieve
the a report download link. It takes the following arguments:

- `report_id`:Unique identifier for the report.

Raises `telstra.messaging.exceptions.ReportsError` if anything goes wrong.

It returns an object with the following properties:

- `report_id`: Use this UUID with our other endpoints to fetch the report.
- `report_status`: The status of the report.
- `report_url`: Download link to download the CSV file.

For example:

```python
# Get a report download link
from telstra.messaging import reports

report_response = reports.get(report_id = '6940c774-4335-4d2b-b758-4ecb19412e85')
print(report_response)
```

### Fetch all reports

Fetch details of all reports recently generated for your account.
Use it to check the status of a report, plus fetch the report ID,
status, report type and expiry date.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#Fetchallreports>.

The function `telstra.messaging.reports.get_all` can be used to fetch
all reports. It doesn't take any arguments.

Raises `telstra.messaging.exceptions.ReportsError` if anything goes wrong.

It returns a list of objects with the following properties:

- `report_id`: Use this UUID with our other endpoints to fetch the report.
- `report_status`: The status of the report.
- `report_type`: The type of report generated.
- `report_expiry`: The expiry date of your report. After this date,
  you will be unable to download your report.

For example:

```python
# Get all reports
from telstra.messaging import reports

reply = reports.get_all()
print(reply)
```

## Health Check

### Get operational status of the messaging service

Check the operational status of the messaging service.
For more information, please see here:
<https://dev.telstra.com/docs/messaging-api/apiReference/apiReferenceOverviewEndpoints?version=3.x#HealthCheck>.

The function `telstra.messaging.health_check.get` can be used to get the status.
It takes no arguments.

Raises `telstra.messaging.exceptions.HealthCheckError` if anything goes wrong.

It returns nothing.

For example:

```python
# Get health check
from telstra.messaging import health_check

try:
  health_check.get()
except HealthCheckError as e
  print(e)
```

## Exceptions

All exceptions that can be raised derive from `MessagingBaseException`:

```python
from telstra.messaging.exceptions import MessagingBaseException
```
