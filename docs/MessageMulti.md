# MessageMulti

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Phone number (in E.164 format) to send the SMS to. This number can be in international format &#x60;\&quot;to\&quot;: \&quot;+61412345678\&quot;&#x60; or in national format.  | [optional] 
**body** | **str** | The text body of the message. Messages longer than 160 characters will be counted as multiple messages.  This field contains the message text, this can be up to 1900 (for a single recipient) or 500 (for multiple recipients) UTF-8 characters. As mobile devices rarely support the full range of UTF-8 characters, it is possible that some characters may not be translated correctly by the mobile device  | [optional] 
**receipt_off** | **bool** | Whether Delivery Receipt will be sent back or not.  Setting this field to &#x60;true&#x60; will disable Delivery Receipts. The &#x60;notifyURL&#x60; field will be ignored, if there is one in the payload. An \&quot;OLD-NONEXISTANT-MESSAGE-ID\&quot; 400 error will also be returned upon Polling for the SMS Status.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


