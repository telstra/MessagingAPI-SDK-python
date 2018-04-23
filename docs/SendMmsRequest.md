# SendMmsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | This will be the source address that will be displayed on the receiving device. If it is not present then it will default to the MSISDN assigned to the app. If replyRequest is set to true, then this field will be ignored. | 
**to** | **str** | This is the destination address. | 
**subject** | **str** | The subject that will be used in an MMS message. | 
**reply_request** | **bool** | If set to true, the reply message functionality will be implemented and the to address will be ignored if present. | 
**notify_url** | **str** | Notify url | [optional] 
**mms_content** | [**list[MMSContent]**](MMSContent.md) | An Array of content that will be sent in an MMS message. If this array is present it will cause the body element to be ignored, and the message will be sent as an MMS. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


