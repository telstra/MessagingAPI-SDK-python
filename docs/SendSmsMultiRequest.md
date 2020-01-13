# SendSmsMultiRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_multi** | [**list[MessageMulti]**](MessageMulti.md) | Multiple SMS. Up to 10 messages can be sent in one API call. | [optional] 
**notiy_url** | **str** | Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc. Please refer to the Delivery Status section for more information.  If you are using a domain URL you must include the forward slash at the end of the URL (e.g. http://www.example.com/).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


