# Telstra_Messaging.ProvisioningApi

All URIs are relative to *https://tapi.telstra.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](ProvisioningApi.md#create_subscription) | **POST** /messages/provisioning/subscriptions | Create Subscription
[**delete_subscription**](ProvisioningApi.md#delete_subscription) | **DELETE** /messages/provisioning/subscriptions | Delete Subscription
[**get_subscription**](ProvisioningApi.md#get_subscription) | **GET** /messages/provisioning/subscriptions | Get Subscription


# **create_subscription**
> ProvisionNumberResponse create_subscription(authorization, body)

Create Subscription

Provision a mobile number

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
api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(configuration))
authorization = 'authorization_example' # str | An OAUTH bearer token that is entitled to use the 'SUBSCRIPTION' scope.
body = Telstra_Messaging.ProvisionNumberRequest() # ProvisionNumberRequest | A JSON payload containing the required attributes

try:
    # Create Subscription
    api_response = api_instance.create_subscription(authorization, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| An OAUTH bearer token that is entitled to use the &#39;SUBSCRIPTION&#39; scope. | 
 **body** | [**ProvisionNumberRequest**](ProvisionNumberRequest.md)| A JSON payload containing the required attributes | 

### Return type

[**ProvisionNumberResponse**](ProvisionNumberResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(authorization)

Delete Subscription

Delete a mobile number subscription from an account

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
api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(configuration))
authorization = 'authorization_example' # str | An OAUTH bearer token that is entitled to use the 'SUBSCRIPTION' scope.

try:
    # Delete Subscription
    api_instance.delete_subscription(authorization)
except ApiException as e:
    print("Exception when calling ProvisioningApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| An OAUTH bearer token that is entitled to use the &#39;SUBSCRIPTION&#39; scope. | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> list[ProvisionNumberResponse] get_subscription(authorization)

Get Subscription

Get mobile number subscription for an account

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
api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(configuration))
authorization = 'authorization_example' # str | An OAUTH bearer token that is entitled to use the 'SUBSCRIPTION' scope.

try:
    # Get Subscription
    api_response = api_instance.get_subscription(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisioningApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| An OAUTH bearer token that is entitled to use the &#39;SUBSCRIPTION&#39; scope. | 

### Return type

[**list[ProvisionNumberResponse]**](ProvisionNumberResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

