# MessageSentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**list[Message]**](Message.md) | An array of messages. | 
**message_type** | **str** | This returns whether the message sent was a SMS or MMS. | 
**number_segments** | **int** | For SMS messages only, the value indicates the number of 160 character message segments sent. | 
**number_national_destinations** | **int** | This returns the number of domestic Australian messages sent. | [optional] 
**number_international_destinations** | **int** | This returns the number of international messages sent | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


