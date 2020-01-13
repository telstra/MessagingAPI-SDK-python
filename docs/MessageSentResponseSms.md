# MessageSentResponseSms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**list[Message]**](Message.md) | An array of messages. | 
**country** | **list[object]** | An array of the countries to which the destination MSISDNs belong. | [optional] 
**message_type** | **str** | This returns whether the message sent was a SMS or MMS. | 
**number_segments** | **int** | A message which has 160 GSM-7 characters or less will have numberSegments&#x3D;1. Note that multi-part messages which are over 160 GSM-7 characters will include the User Data Header as part of the numberSegments. The User Data Header is being used for the re-assembly of the messages.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


