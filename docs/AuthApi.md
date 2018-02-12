# Telstra_Messaging.AuthApi

All URIs are relative to *https://tapi.telstra.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_token_post**](AuthApi.md#oauth_token_post) | **POST** /oauth/token | AuthGeneratetokenPost


# **oauth_token_post**
> AuthgeneratetokenpostResponse oauth_token_post(o_auth_client_id, o_auth_client_secret)

AuthGeneratetokenPost

generate auth token

### Example
```python
from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Telstra_Messaging.AuthApi()
o_auth_client_id = 'o_auth_client_id_example' # str | 
o_auth_client_secret = 'o_auth_client_secret_example' # str | 

try:
    # AuthGeneratetokenPost
    api_response = api_instance.oauth_token_post(o_auth_client_id, o_auth_client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->oauth_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_client_id** | **str**|  | 
 **o_auth_client_secret** | **str**|  | 

### Return type

[**AuthgeneratetokenpostResponse**](AuthgeneratetokenpostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

