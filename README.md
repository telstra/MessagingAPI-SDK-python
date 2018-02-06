# Telstra_Messaging
 The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages. 

- API version: 2.2.4
- Package version: 1.0.1

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install


```sh
pip install git+https://github.com/Telstra/Messaging-SDK-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Telstra/Messaging-SDK-python.git`)

```python
import Telstra_Messaging 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

```python
import Telstra_Messaging
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Telstra_Messaging.AuthenticationApi()
client_id = 'client_id_example' # str | 
client_secret = 'client_secret_example' # str | 
grant_type = 'client_credentials' # str |  (default to client_credentials)

try:
    # Generate authentication token
    api_response = api_instance.auth_token(client_id, client_secret, grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_token: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://tapi.telstra.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MessagingApi* | [**get_mms_status**](docs/MessagingApi.md#get_mms_status) | **GET** /messages/mms/{messageid}/status | Get MMS Status
*MessagingApi* | [**get_sms_status**](docs/MessagingApi.md#get_sms_status) | **GET** /messages/sms/{messageId}/status | Get SMS Status
*MessagingApi* | [**retrieve_sms_responses**](docs/MessagingApi.md#retrieve_sms_responses) | **GET** /messages/sms | Retrieve SMS Responses
*MessagingApi* | [**send_mms**](docs/MessagingApi.md#send_mms) | **POST** /messages/mms | Send MMS
*MessagingApi* | [**send_sms**](docs/MessagingApi.md#send_sms) | **POST** /messages/sms | Send SMS
*ProvisioningApi* | [**create_subscription**](docs/ProvisioningApi.md#create_subscription) | **POST** /messages/provisioning/subscriptions | Create Subscription
*ProvisioningApi* | [**delete_subscription**](docs/ProvisioningApi.md#delete_subscription) | **DELETE** /messages/provisioning/subscriptions | Delete Subscription
*ProvisioningApi* | [**get_subscription**](docs/ProvisioningApi.md#get_subscription) | **GET** /messages/provisioning/subscriptions | Get Subscription
*AuthenticationApi* | [**auth_token**](docs/AuthenticationApi.md#auth_token) | **POST** /oauth/token | Generate authentication token


## Documentation For Models

 - [ErrorError](docs/ErrorError.md)
 - [ErrorErrorError](docs/ErrorErrorError.md)
 - [InboundPollResponse](docs/InboundPollResponse.md)
 - [MMSContent](docs/MMSContent.md)
 - [Message](docs/Message.md)
 - [MessageSentResponse](docs/MessageSentResponse.md)
 - [MessageType](docs/MessageType.md)
 - [OAuthRequest](docs/OAuthRequest.md)
 - [OAuthResponse](docs/OAuthResponse.md)
 - [OutboundPollResponse](docs/OutboundPollResponse.md)
 - [ProvisionNumberRequest](docs/ProvisionNumberRequest.md)
 - [ProvisionNumberResponse](docs/ProvisionNumberResponse.md)
 - [SendMmsRequest](docs/SendMmsRequest.md)
 - [SendSMSRequest](docs/SendSMSRequest.md)
 - [Status](docs/Status.md)


## Documentation For Authorization


## auth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **NSMS**: NSMS


## Author



