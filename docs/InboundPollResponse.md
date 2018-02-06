# InboundPollResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The phone number (recipient) that the message was sent to(in E.164 format). | [optional] 
**_from** | **str** | The phone number (sender) that the message was sent from (in E.164 format). | [optional] 
**body** | **str** | Text body of the message that was sent | [optional] 
**received_timestamp** | **str** | The date and time when the message was recieved by recipient. | [optional] 
**more_messages** | **int** | Indicates if there are more messages that can be polled from the server. 0&#x3D;No more messages available. Anything else indicates there are more messages on the server. | [optional] 
**message_id** | **str** | Optional message ID of the SMS you sent. Use this ID to view the message status or get responses. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


