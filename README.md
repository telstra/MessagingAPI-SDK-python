# Getting started


The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.

It also allows your application to track the delivery status of both sent and received SMS messages.


## How to Build


You must have Python 2 >=2.7.9 or Python 3 >=3.4 installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

## Initialization

### Example

```python
from telstramessagingapi.telstramessagingapi_client import TelstramessagingapiClient
from telstramessagingapi.models.o_auth_scope_enum import OAuthScopeEnum
from telstramessagingapi.exceptions.o_auth_provider_exception import OAuthProviderException

# Configuration parameters and credentials
o_auth_client_id = 'o_auth_client_id' # OAuth 2 Client ID
o_auth_client_secret = 'o_auth_client_secret' # OAuth 2 Client Secret

#  create a new client
client = TelstramessagingapiClient(o_auth_client_id, o_auth_client_secret)

token = client.auth.authorize([OAuthScopeEnum.NSMS])

# the client is now authorized and you can use controllers to make endpoint calls
```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [ProvisioningController](#provisioning_controller)
* [MessagingController](#messaging_controller)

## <a name="provisioning_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ProvisioningController") ProvisioningController

### Get controller instance

An instance of the ``` ProvisioningController ``` class can be accessed from the API Client.

```python
 provisioning_client = client.provisioning
```

### <a name="delete_subscription"></a>![Method: ](https://apidocs.io/img/method.png ".ProvisioningController.delete_subscription") delete_subscription

> Delete Subscription

#### Example Usage

```python

provisioning_client.delete_subscription()

```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid or missing request parameters |
| 401 | Invalid or no credentials passed in the request |
| 403 | Authorization credentials passed and accepted but account does not have permission |
| 404 | The requested URI does not exist |
| 0 | An internal error occurred when processing the request |




### <a name="create_subscription"></a>![Method: ](https://apidocs.io/img/method.png ".ProvisioningController.create_subscription") create_subscription

> Create Subscription

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | A JSON payload containing the required attributes |



#### Example Usage

```python
body = ProvisionNumberRequest()

result = provisioning_client.create_subscription(body)

```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid or missing request parameters |
| 401 | Invalid or no credentials passed in the request |
| 403 | Authorization credentials passed and accepted but account does not have permission |
| 404 | The requested URI does not exist |
| 0 | An internal error occurred when processing the request |




### <a name="get_subscription"></a>![Method: ](https://apidocs.io/img/method.png ".ProvisioningController.get_subscription") get_subscription

> Get Subscription

#### Example Usage

```python

result = provisioning_client.get_subscription()

```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid or missing request parameters |
| 401 | Invalid or no credentials passed in the request |
| 403 | Authorization credentials passed and accepted but account does not have permission |
| 404 | The requested URI does not exist |
| 0 | An internal error occurred when processing the request |




[Back to List of Controllers](#list_of_controllers)

## <a name="messaging_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MessagingController") MessagingController

### Get controller instance

An instance of the ``` MessagingController ``` class can be accessed from the API Client.

```python
 messaging_client = client.messaging
```

### <a name="retrieve_sms_responses"></a>![Method: ](https://apidocs.io/img/method.png ".MessagingController.retrieve_sms_responses") retrieve_sms_responses

> Retrieve SMS Responses

#### Example Usage

```python

result = messaging_client.retrieve_sms_responses()

```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid or missing request parameters |
| 401 | Invalid or no credentials passed in the request |
| 403 | Authorization credentials passed and accepted but account does<br>not have permission |
| 404 | The requested URI does not exist |
| 405 | The requested resource does not support the supplied verb |
| 415 | API does not support the requested content type |
| 422 | The request is formed correctly, but due to some condition<br>the request cannot be processed e.g. email is required and it is not provided<br>in the request |
| 501 | The HTTP method being used has not yet been implemented for<br>the requested resource |
| 503 | The service requested is currently unavailable |
| 0 | An internal error occurred when processing the request |




### <a name="create_send_sms"></a>![Method: ](https://apidocs.io/img/method.png ".MessagingController.create_send_sms") create_send_sms

> Send SMS

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| payload |  ``` Required ```  | A JSON or XML payload containing the recipient's phone number and text message.

The recipient number should be in the format '04xxxxxxxx' where x is a digit |



#### Example Usage

```python
payload = SendSMSRequest()

result = messaging_client.create_send_sms(payload)

```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid or missing request parameters |
| 401 | Invalid or no credentials passed in the request |
| 403 | Authorization credentials passed and accepted but account does<br>not have permission |
| 404 | The requested URI does not exist |
| 405 | The requested resource does not support the supplied verb |
| 415 | API does not support the requested content type |
| 422 | The request is formed correctly, but due to some condition<br>the request cannot be processed e.g. email is required and it is not provided<br>in the request |
| 501 | The HTTP method being used has not yet been implemented for<br>the requested resource |
| 503 | The service requested is currently unavailable |
| 0 | An internal error occurred when processing the request |




### <a name="get_sms_status"></a>![Method: ](https://apidocs.io/img/method.png ".MessagingController.get_sms_status") get_sms_status

> Get SMS Status

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageId |  ``` Required ```  | Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms |



#### Example Usage

```python
message_id = 'messageId'

result = messaging_client.get_sms_status(message_id)

```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid or missing request parameters |
| 401 | Invalid or no credentials passed in the request |
| 403 | Authorization credentials passed and accepted but account does<br>not have permission |
| 404 | The requested URI does not exist |
| 405 | The requested resource does not support the supplied verb |
| 415 | API does not support the requested content type |
| 422 | The request is formed correctly, but due to some condition<br>the request cannot be processed e.g. email is required and it is not provided<br>in the request |
| 501 | The HTTP method being used has not yet been implemented for<br>the requested resource |
| 503 | The service requested is currently unavailable |
| 0 | An internal error occurred when processing the request |


### <a name="create_send_mms"></a>![Method: ](https://apidocs.io/img/method.png ".MessagingController.create_send_mms") create_send_mms

> Send MMS

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | A JSON or XML payload containing the recipient's phone number
and MMS message.The recipient number should be in the format '04xxxxxxxx'
where x is a digit |



#### Example Usage

```python
body = SendMMSRequest()

result = messaging_client.create_send_mms(body)

```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid or missing request parameters |
| 401 | Invalid or no credentials passed in the request |
| 403 | Authorization credentials passed and accepted but account does<br>not have permission |
| 404 | The requested URI does not exist |
| 405 | The requested resource does not support the supplied verb |
| 415 | API does not support the requested content type |
| 422 | The request is formed correctly, but due to some condition<br>the request cannot be processed e.g. email is required and it is not provided<br>in the request |
| 501 | The HTTP method being used has not yet been implemented for<br>the requested resource |
| 503 | The service requested is currently unavailable |
| 0 | An internal error occurred when processing the request |




### <a name="get_mms_status"></a>![Method: ](https://apidocs.io/img/method.png ".MessagingController.get_mms_status") get_mms_status

> Get MMS Status

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageid |  ``` Required ```  | Unique identifier of a message - it is the value returned from
a previous POST call to https://api.telstra.com/v2/messages/mms |



#### Example Usage

```python
messageid = 'messageid'

result = messaging_client.get_mms_status(messageid)

```

See the documentation at [Dev.Telstra.com](https://dev.telstra.com/content/messaging-api) for more information

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid or missing request parameters |
| 401 | Invalid or no credentials passed in the request |
| 403 | Authorization credentials passed and accepted but account does<br>not have permission |
| 404 | The requested URI does not exist |
| 405 | The requested resource does not support the supplied verb |
| 415 | API does not support the requested content type |
| 422 | The request is formed correctly, but due to some condition<br>the request cannot be processed e.g. email is required and it is not provided<br>in the request |
| 501 | The HTTP method being used has not yet been implemented for<br>the requested resource |
| 503 | The service requested is currently unavailable |
| 0 | An internal error occurred when processing the request |




[Back to List of Controllers](#list_of_controllers)



