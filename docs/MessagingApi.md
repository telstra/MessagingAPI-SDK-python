# Telstra_Messaging.MessagingApi

All URIs are relative to *https://tapi.telstra.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mms_status**](MessagingApi.md#get_mms_status) | **GET** /messages/mms/{messageid}/status | Get MMS Status
[**get_sms_status**](MessagingApi.md#get_sms_status) | **GET** /messages/sms/{messageId}/status | Get SMS Status
[**retrieve_mms_responses**](MessagingApi.md#retrieve_mms_responses) | **GET** /messages/mms | Retrieve MMS Responses
[**retrieve_sms_responses**](MessagingApi.md#retrieve_sms_responses) | **GET** /messages/sms | Retrieve SMS Responses
[**send_mms**](MessagingApi.md#send_mms) | **POST** /messages/mms | Send MMS
[**send_sms**](MessagingApi.md#send_sms) | **POST** /messages/sms | Send SMS


# **get_mms_status**
> list[OutboundPollResponse] get_mms_status(messageid)

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
 **messageid** | **str**| Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms  | 

### Return type

[**list[OutboundPollResponse]**](OutboundPollResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sms_status**
> list[OutboundPollResponse] get_sms_status(message_id)

Get SMS Status

If no notification URL has been specified, it is possible to poll for the message status. Note that the `MessageId` that appears in the URL must be URL encoded. Just copying the `MessageId` as it was supplied when submitting the message may not work.  SMS Status with Notification URL --- When a message has reached its final state, the API will send a POST to the URL that has been previously specified. <pre><code class=\"language-sh\">{     to: '+61418123456'     sentTimestamp: '2017-03-17T10:05:22+10:00'     receivedTimestamp: '2017-03-17T10:05:23+10:00'     messageId: /cccb284200035236000000000ee9d074019e0301/1261418123456     deliveryStatus: DELIVRD   } </code></pre>  The fields are: <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>to</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>deliveryStatus</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>messageId</code></td>       <td>The same reference that was returned when the original message was sent.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>   </tbody> </table>  Upon receiving this call it is expected that your servers will give a 204 (No Content) response. Anything else will cause the API to reattempt the call 5 minutes later. 

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
message_id = 'message_id_example' # str | Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms. 

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
 **message_id** | **str**| Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms.  | 

### Return type

[**list[OutboundPollResponse]**](OutboundPollResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_mms_responses**
> list[MMSContent] retrieve_mms_responses()

Retrieve MMS Responses

Messages are retrieved one at a time, starting with the earliest response. If the subscription has a `notifyURL`, response messages will be logged there instead.  # Notification URL Format for MMS Replies  <pre><code class=\"language-sh\">{   \"status\": \"RECEIVED\",   \"destinationAddress\": \"+61418123456\",   \"senderAddress\": \"+61421987654\",   \"subject\": \"Foo\",   \"sentTimestamp\": \"2018-03-23T12:15:45+10:00\",   \"envelope\": \"string\",   \"MMSContent\":     [       {         \"type\": \"text/plain\",         \"filename\": \"text_1.txt\",         \"payload\": \"string\"       },       {         \"type\": \"image/jpeg\",         \"filename\": \"sample.jpeg\",         \"payload\": \"string\"       }     ] }</code></pre>  The fields are: | Field | Description | | --- | --- | | `status` | The final state of the message. | | `destinationAddress` |The number the message was sent to. | | `senderAddress` | The number the message was sent from. | | `subject` | The subject assigned to the message. | | `sentTimestamp` | Time handling of the message ended. | | `envelope` | Information about about terminal type and originating operator. | | `MMSContent` | An array of the actual content of the reply message. | | `type` | The content type of the message. | | `filename` | The filename for the message content. | | `payload` | The content of the message. | 

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
    # Retrieve MMS Responses
    api_response = api_instance.retrieve_mms_responses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->retrieve_mms_responses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MMSContent]**](MMSContent.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_sms_responses**
> InboundPollResponse retrieve_sms_responses()

Retrieve SMS Responses

Messages are retrieved one at a time, starting with the earliest response. The API supports the encoding of the full range of emojis in the reply message. The emojis will be in their UTF-8 format. If the subscription has a `notifyURL`, response messages will be logged there instead.  # Notification URL Format for SMS Response  <pre><code class=\"language-sh\">{   \"to\":\"+61472880123\",   \"from\":\"+61412345678\",   \"body\":\"Foo4\",   \"sentTimestamp\":\"2018-04-20T14:24:35\",   \"messageId\":\"DMASApiA0000000146\" }</code></pre>  The fields are: | Field | Description | | --- |--- | | `to` | The number the message was sent to. | | `from` | The number the message was sent from. | | `body` | The content of the SMS response. | | `sentTimestamp` | Time handling of the message ended. | | `messageId` | The ID assigned to the message. | 

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

[**InboundPollResponse**](InboundPollResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_mms**
> MessageSentResponse send_mms(send_mms_request)

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
send_mms_request = Telstra_Messaging.SendMmsRequest() # SendMmsRequest | A JSON or XML payload containing the recipient's phone number and MMS message.
The recipient number should be in the format '04xxxxxxxx' where x is a digit.


try:
    # Send MMS
    api_response = api_instance.send_mms(send_mms_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->send_mms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_mms_request** | [**SendMmsRequest**](SendMmsRequest.md)| A JSON or XML payload containing the recipient&#39;s phone number and MMS message.
The recipient number should be in the format &#39;04xxxxxxxx&#39; where x is a digit.
 | 

### Return type

[**MessageSentResponse**](MessageSentResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms**
> MessageSentResponse send_sms(send_sms_request)

Send SMS

Send an SMS Message to a single or multiple mobile number/s. 

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
send_sms_request = Telstra_Messaging.SendSMSRequest() # SendSMSRequest | A JSON or XML payload containing the recipient's phone number and text message.
This number can be in international format if preceeded by a '+' or in national format ('04xxxxxxxx') where x is a digit.


try:
    # Send SMS
    api_response = api_instance.send_sms(send_sms_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->send_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_sms_request** | [**SendSMSRequest**](SendSMSRequest.md)| A JSON or XML payload containing the recipient&#39;s phone number and text message.
This number can be in international format if preceeded by a &#39;+&#39; or in national format (&#39;04xxxxxxxx&#39;) where x is a digit.
 | 

### Return type

[**MessageSentResponse**](MessageSentResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

