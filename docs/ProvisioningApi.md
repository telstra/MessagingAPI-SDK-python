# Telstra_Messaging.ProvisioningApi

All URIs are relative to *https://tapi.telstra.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](ProvisioningApi.md#create_subscription) | **POST** /messages/provisioning/subscriptions | Create Subscription
[**delete_subscription**](ProvisioningApi.md#delete_subscription) | **DELETE** /messages/provisioning/subscriptions | Delete Subscription
[**get_subscription**](ProvisioningApi.md#get_subscription) | **GET** /messages/provisioning/subscriptions | Get Subscription


# **create_subscription**
> ProvisionNumberResponse create_subscription(body)

Create Subscription

Invoke the provisioning API to get a dedicated mobile number for an account or application.  Note that Free Trial apps will have a 30-Day Limit for their provisioned number. If the Provisioning call is made several times within that 30-Day period, it will return the `expiryDate` in the Unix format and will not add any activeDays until after that `expiryDate`. After the `expiryDate`, you may make another Provisioning call to extend the activeDays by another 30-Days.  For paid apps, a provisioned number can be allotted for a maximum of 5 years. If a Provisioning call is made which will result to activeDays > 1825, a 409 `Active Days Max` response will be returned to indicate that the provisioned number is already valid for more than 5 years and that no update to activeDays has been made. 

### Example

* OAuth Authentication (auth):
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint
configuration = Telstra_Messaging.Configuration()
# Configure OAuth2 access token for authorization: auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://tapi.telstra.com/v2
configuration.host = "https://tapi.telstra.com/v2"
# Create an instance of the API class
api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(configuration))
body = Telstra_Messaging.ProvisionNumberRequest() # ProvisionNumberRequest | A JSON payload containing the required attributes

try:
    # Create Subscription
    api_response = api_instance.create_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvisionNumberRequest**](ProvisionNumberRequest.md)| A JSON payload containing the required attributes | 

### Return type

[**ProvisionNumberResponse**](ProvisionNumberResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid or missing request parameters |  -  |
**401** | Invalid access token. Please try with a valid token |  -  |
**403** | Authorization credentials passed and accepted but account does not have permission  SpikeArrest-The API call rate limit has been exceeded |  -  |
**404** | The requested URI does not exist  RESOURCE-NOT-FOUND  |  -  |
**409** | Active Days Max. You can no longer update or add to activeDays because it already exceeds more than 5 years. |  -  |
**500** | Technical error : Unable to route the message to a Target Endpoint : An error has occurred while processing your request, please refer to API Docs for summary on the issue  |  -  |
**0** | An internal error occurred when processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(body)

Delete Subscription

Delete a mobile number subscription from an account 

### Example

* OAuth Authentication (auth):
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint
configuration = Telstra_Messaging.Configuration()
# Configure OAuth2 access token for authorization: auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://tapi.telstra.com/v2
configuration.host = "https://tapi.telstra.com/v2"
# Create an instance of the API class
api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(configuration))
body = Telstra_Messaging.DeleteNumberRequest() # DeleteNumberRequest | EmptyArr

try:
    # Delete Subscription
    api_instance.delete_subscription(body)
except ApiException as e:
    print("Exception when calling ProvisioningApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteNumberRequest**](DeleteNumberRequest.md)| EmptyArr | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Invalid or missing request parameters |  -  |
**401** | Invalid access token. Please try with a valid token |  -  |
**403** | Authorization credentials passed and accepted but account does not have permission  SpikeArrest-The API call rate limit has been exceeded |  -  |
**404** | The requested URI does not exist  RESOURCE-NOT-FOUND |  -  |
**500** | Technical error : Unable to route the message to a Target Endpoint : An error has occurred while processing your request, please refer to API Docs for summary on the issue |  -  |
**0** | An internal error occurred when processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> GetSubscriptionResponse get_subscription()

Get Subscription

Get mobile number subscription for an account 

### Example

* OAuth Authentication (auth):
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint
configuration = Telstra_Messaging.Configuration()
# Configure OAuth2 access token for authorization: auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://tapi.telstra.com/v2
configuration.host = "https://tapi.telstra.com/v2"
# Create an instance of the API class
api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(configuration))

try:
    # Get Subscription
    api_response = api_instance.get_subscription()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningApi->get_subscription: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSubscriptionResponse**](GetSubscriptionResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid or missing request parameters |  -  |
**401** | Invalid access token. Please try with a valid token |  -  |
**403** | Authorization credentials passed and accepted but account does not have permission  SpikeArrest-The API call rate limit has been exceeded |  -  |
**404** | The requested URI does not exist  RESOURCE-NOT-FOUND |  -  |
**500** | Technical error : Unable to route the message to a Target Endpoint : An error has occurred while processing your request, please refer to API Docs for summary on the issue |  -  |
**0** | An internal error occurred when processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

