# Telstra_Messaging.MessagingApi

All URIs are relative to *https://tapi.telstra.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mms_status**](MessagingApi.md#get_mms_status) | **GET** /messages/mms/{messageid}/status | Get MMS Status
[**get_sms_status**](MessagingApi.md#get_sms_status) | **GET** /messages/sms/{messageId}/status | Get SMS Status
[**retrieve_sms_responses**](MessagingApi.md#retrieve_sms_responses) | **GET** /messages/sms | Retrieve SMS Responses
[**send_mms**](MessagingApi.md#send_mms) | **POST** /messages/mms | Send MMS
[**send_sms**](MessagingApi.md#send_sms) | **POST** /messages/sms | Send SMS


# **get_mms_status**
> OutboundPollResponse get_mms_status(messageid)

Get MMS Status

Get MMS Status

### Example
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = Telstra_Messaging.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = Telstra_Messaging.MessagingApi(Telstra_Messaging.ApiClient(configuration))
messageid = 'messageid_example' # str | Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms

try:
    # Get MMS Status
    api_response = api_instance.get_mms_status(messageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_mms_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **messageid** | **str**| Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms | 

### Return type

[**OutboundPollResponse**](OutboundPollResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sms_status**
> OutboundPollResponse get_sms_status(message_id)

Get SMS Status

Get Message Status

### Example
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = Telstra_Messaging.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = Telstra_Messaging.MessagingApi(Telstra_Messaging.ApiClient(configuration))
message_id = 'message_id_example' # str | Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms

try:
    # Get SMS Status
    api_response = api_instance.get_sms_status(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_sms_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms | 

### Return type

[**OutboundPollResponse**](OutboundPollResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_sms_responses**
> list[InboundPollResponse] retrieve_sms_responses()

Retrieve SMS Responses

Retrieve Messages

### Example
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = Telstra_Messaging.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = Telstra_Messaging.MessagingApi(Telstra_Messaging.ApiClient(configuration))

try:
    # Retrieve SMS Responses
    api_response = api_instance.retrieve_sms_responses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->retrieve_sms_responses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InboundPollResponse]**](InboundPollResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_mms**
> object send_mms(body)

Send MMS

Send MMS

### Example
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = Telstra_Messaging.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = Telstra_Messaging.MessagingApi(Telstra_Messaging.ApiClient(configuration))
body = Telstra_Messaging.SendMmsRequest() # SendMmsRequest | A JSON or XML payload containing the recipient's phone number and MMS message.The recipient number should be in the format '04xxxxxxxx' where x is a digit

try:
    # Send MMS
    api_response = api_instance.send_mms(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->send_mms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendMmsRequest**](SendMmsRequest.md)| A JSON or XML payload containing the recipient&#39;s phone number and MMS message.The recipient number should be in the format &#39;04xxxxxxxx&#39; where x is a digit | 

### Return type

**object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms**
> MessageSentResponse send_sms(payload)

Send SMS

Send Message

### Example
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = Telstra_Messaging.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = Telstra_Messaging.MessagingApi(Telstra_Messaging.ApiClient(configuration))
payload = Telstra_Messaging.SendSMSRequest() # SendSMSRequest | A JSON or XML payload containing the recipient's phone number and text message. The recipient number should be in the format '04xxxxxxxx' where x is a digit

try:
    # Send SMS
    api_response = api_instance.send_sms(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->send_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**SendSMSRequest**](SendSMSRequest.md)| A JSON or XML payload containing the recipient&#39;s phone number and text message. The recipient number should be in the format &#39;04xxxxxxxx&#39; where x is a digit | 

### Return type

[**MessageSentResponse**](MessageSentResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

