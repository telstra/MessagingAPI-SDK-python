# Telstra_Messaging
 The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages. 


- API version: 2.2.4
- Package version: 1.0.2

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install


```sh
pip install git+https://github.com/Telstra/MessagingAPI-SDK-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Telstra/MessagingAPI-SDK-python.git`)

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

# Configure OAuth2 access token for authorization: auth
Telstra_Messaging.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = Telstra_Messaging.MessagingApi()
messageid = 'messageid_example' # str | Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms

try:
    # Get MMS Status
    api_response = api_instance.get_mms_status(messageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_mms_status: %s\n" % e)

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

 - [DeleteNumberRequest](docs/DeleteNumberRequest.md)
 - [ErrorError](docs/ErrorError.md)
 - [ErrorErrorError](docs/ErrorErrorError.md)
 - [GetSubscriptionResponse](docs/GetSubscriptionResponse.md)
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


## Documentation For Authorisation


## auth

- **Type**: OAuth
- **Flow**: application
- **Authorisation URL**: 
- **Scopes**: 
 - **NSMS**: NSMS


## Author



