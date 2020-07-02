# ProvisionNumberRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_days** | **int** | The number of days before for which this number is provisioned.  | [optional] 
**notify_url** | **str** | A notification URL that will be POSTed to whenever a new message (i.e. a reply to a message sent) arrives at this destination address.  If this is not provided then you can use the Get /sms or /mms API to poll for reply messages.  If you are using a domain URL you must include the forward slash at the end of the URL (e.g. http://www.example.com/).  *Please note that the notification URLs and the Get /sms or /mms call are exclusive. If a notification URL has been set then the GET call will not provide any useful information.*  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


