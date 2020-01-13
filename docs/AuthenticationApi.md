# Telstra_Messaging.AuthenticationApi

All URIs are relative to *https://tapi.telstra.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_token**](AuthenticationApi.md#auth_token) | **POST** /oauth/token | Generate OAuth2 token


# **auth_token**
> OAuthResponse auth_token(client_id, client_secret, grant_type, scope=scope)

Generate OAuth2 token

To generate an OAuth2 Authentication token, pass through your `Client key` and `Client secret` that you received when you registered for the **API Free Trial** Product.  The grant_type should be left as `client_credentials` and the scope as `NSMS`.  The token will expire in one hour. 

### Example

```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = Telstra_Messaging.AuthenticationApi()
client_id = 'client_id_example' # str | 
client_secret = 'client_secret_example' # str | 
grant_type = 'client_credentials' # str |  (default to 'client_credentials')
scope = 'scope_example' # str | NSMS (optional)

try:
    # Generate OAuth2 token
    api_response = api_instance.auth_token(client_id, client_secret, grant_type, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 
 **grant_type** | **str**|  | [default to &#39;client_credentials&#39;]
 **scope** | **str**| NSMS | [optional] 

### Return type

[**OAuthResponse**](OAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | unsupported_grant_type |  -  |
**401** | invalid_client |  -  |
**404** | The requested URI does not exist |  -  |
**503** | The service requested is currently unavailable |  -  |
**0** | An internal error occurred when processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

