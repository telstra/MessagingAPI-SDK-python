# GetMmsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The final state of the message.  | 
**destination_address** | **str** | The number the message was sent to.  | 
**sender_address** | **str** | The number the message was sent from.  | 
**subject** | **str** | The subject assigned to the message.  | [optional] 
**message_id** | **str** | Message Id assigned by the MMSC.  | [optional] 
**api_msg_id** | **str** | Message Id assigned by the API.  | [optional] 
**sent_timestamp** | **str** | Time handling of the message ended.  | 
**mms_content** | [**list[MMSContent]**](MMSContent.md) | An array of content that was received in an MMS message.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


