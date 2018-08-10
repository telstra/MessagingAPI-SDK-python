# coding: utf-8

"""
    Telstra Messaging API

     # Introduction  <table><tbody><tr><td class = 'into_api' style='border:none;padding:0 0 0 0'><p>Send and receive SMS and MMS messages globally using Telstra's enterprise grade Messaging API. It also allows your application to track the delivery status of both sent and received messages. Get your dedicated Australian number, and start sending and receiving messages today.</p></td><td class = 'into_api_logo' style='width: 20%;border:none'><img class = 'api_logo' style='margin: -26px 0 0 0' src = 'https://test-telstra-retail-tdev.devportal.apigee.io/sites/default/files/messagingapi-icon.png'></td></tr></tbody></table>  # Features  The Telstra Messaging API provides the features below. | Feature | Description | | --- | --- | | `Dedicated Number` | Provision a mobile number for your account to be used as `from` address in the API | | `Send Messages` | Sending SMS or MMS messages | | `Receive Messages` | Telstra will deliver messages sent to a dedicated number or to the `notifyURL` defined by you | | `Broadcast Messages` | Invoke a single API call to send a message to a list of numbers provided in `to` | | `Delivery Status` | Query the delivery status of your messages | | `Callbacks` | Provide a notification URL and Telstra will notify your app when a message status changes | | `Alphanumeric Identifier` | Differentiate yourself by providing an alphanumeric string in `from`. This feature is only available on paid plans | | `Concatenation` | Send messages up to 1900 characters long and Telstra will automaticaly segment and reassemble them | | `Reply Request` | Create a chat session by associating `messageId` and `to` number to track responses received from a mobile number. We will store this association for 8 days | | `Character set` | Accepts all Unicode characters as part of UTF-8 | | `Bounce-back response` | See if your SMS hits an unreachable or unallocated number (Australia Only) | | `Queuing` | Messaging API will automatically queue and deliver each message at a compliant rate. | | `Emoji Encoding` | The API supports the encoding of the full range of emojis. Emojis in the reply messages will be in their UTF-8 format. |  ## Delivery Notification or Callbacks  The API provides several methods for notifying when a message has been delivered to the destination.  1. When you send a message there is an opportunity to specify a `notifyURL`. Once the message has been delivered the API will make a call to this URL to advise of the message status. 2. If you do not specify a URL you can always call the `GET /status` API to get the status of the message.  # Getting Access to the API  1. Register at [https://dev.telstra.com](https://dev.telstra.com). 2. After registration, login to [https://dev.telstra.com](https://dev.telstra.com) and navigate to the **My apps** page. 3. Create your application by clicking the **Add new app** button 4. Select **API Free Trial** Product when configuring your application. This Product includes the Telstra Messaging API as well as other free trial APIs. Your application will be approved automatically. 5. There is a maximum of 1000 free messages per developer. Additional messages and features can be purchased from [https://dev.telstra.com](https://dev.telstra.com). 6. Note your `Client key` and `Client secret` as these will be needed to provision a number for your application and for authentication.  Now head over to **Getting Started** where you can find a postman collection as well as some links to sample apps and SDKs to get you started.  Happy Messaging!  # Frequently Asked Questions  **Q: Is creating a subscription via the Provisioning call a required step?**  A. Yes. You will only be able to start sending messages if you have a provisioned dedicated number. Use Provisioning to create a dedicated number subscription, or renew your dedicated number if it has expired.  **Q: When trying to send an SMS I receive a `400 Bad Request` response. How can I fix this?**  A. You need to make sure you have a provisioned dedicated number before you can send an SMS.  If you do not have a provisioned dedicated number and you try to send a message via the API, you will get the error below in the response:  <pre><code class=\"language-sh\">{   \"status\":\"400\",   \"code\":\"DELIVERY-IMPOSSIBLE\",   \"message\":\"Invalid \\'from\\' address specified\" }</code></pre>  Use Provisioning to create a dedicated number subscription, or renew your dedicated number if it has expired.  **Q: How long does my dedicated number stay active for?**  A. When you provision a dedicated number, by default it will be active for 30 days.  You can use the `activeDays` parameter during the provisioning call to increment or decrement the number of days your dedicated number will remain active.  Note that Free Trial apps will have 30 days as the maximum `activeDays` they can add to their provisioned number. If the Provisioning call is made several times within that 30-Day period, it will return the `expiryDate` in the Unix format and will not add any activeDays until after that `expiryDate`.  **Q: Can I send a broadcast message using the Telstra Messaging API?**  A. Yes. Recipient numbers can be in the form of an array of strings if a broadcast message needs to be sent, allowing you to send to multiple mobile numbers in one API call.   A sample request body for this will be: `{\"to\":[\"+61412345678\",\"+61487654321\"],\"body\":\"Test Message\"}`    **Q: Can I send SMS and MMS to all countries?**  A. You can send SMS and MMS to all countries EXCEPT to countries which are subject to global sanctions namely: Burma, Côte d'Ivoire, Cuba, Iran, North Korea, Syria.  **Q: Can I use `Alphanumeric Identifier` from my paid plan via credit card?**  A. `Alphanumeric Identifier` is only available on Telstra Account paid plans, not through credit card paid plans.  **Q: What is the maximum sized MMS that I can send?**  A. This will depend on the carrier that will receive the MMS. For Telstra it's up to 2MB,  Optus up to 1.5MB and Vodafone only allows up to 500kB. You will need to check with international carriers for thier MMS size limits.  **Q: How is the size of an MMS calculated?**  A. Images are scaled up to approximately 4/3 when base64 encoded. Additionally, there is approximately 200 bytes of overhead on each MMS. Assuming the maximum MMS that can be sent on Telstra’s network is 2MB, then the maximum image size that can be sent will be approximately 1.378MB (1.378 x 1.34 + 200, without SOAP encapsulation).  **Q: How is an MMS classified as Small or Large?**  A. MMSes with size below 600kB are classed as Small whereas those that are bigger than 600kB are classed as Large. They will be charged accordingly.  **Q: Are SMILs supported by the Messaging API?**  A. While there will be no error if you send an MMS with a SMIL presentation, the actual layout or sequence defined in the SMIL may not display as expected because most of the new smartphone devices ignore the SMIL presentation layer. SMIL was used in feature phones which had limited capability and SMIL allowed a *powerpoint type* presentation to be provided. Smartphones now have the capability to display video which is the better option for presentations. It is recommended that MMS messages should just drop the SMIL.  **Q: How do I assign a delivery notification or callback URL?**  A. You can assign a delivery notification or callback URL by adding the `notifyURL` parameter in the body of the request when you send a message. Once the message has been delivered, a notification will then be posted to this callback URL.  **Q: What is the difference between the `notifyURL` parameter in the Provisoning call versus the `notifyURL` parameter in the Send Message call?**  A. The `notifyURL` in the Provisoning call will be the URL where replies to the provisioned number will be posted. On the other hand, the `notifyURL` in the Send Message call will be the URL where the delivery notification will be posted, e.g. when an SMS has already been delivered to the recipient.  # Getting Started  Below are the steps to get started with the Telstra Messaging API.   1. Generate an OAuth2 token using your `Client key` and `Client secret`.   2. Use the Provisioning call to create a subscription and receive a dedicated number.   3. Send a message to a specific mobile number.  ## Run in Postman <a href=\"https://app.getpostman.com/run-collection/ded00578f69a9deba256#?env%5BMessaging%20API%20Environments%5D=W3siZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X2lkIiwidmFsdWUiOiIiLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X3NlY3JldCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6ImFjY2Vzc190b2tlbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Imhvc3QiLCJ2YWx1ZSI6InRhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiQXV0aG9yaXphdGlvbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Im9hdXRoX2hvc3QiLCJ2YWx1ZSI6InNhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoibWVzc2FnZV9pZCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifV0=\"><img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\"/></a>  ## Sample Apps   - [Perl Sample App](https://github.com/telstra/MessagingAPI-perl-sample-app)   - [Happy Chat App](https://github.com/telstra/messaging-sample-code-happy-chat)   - [PHP Sample App](https://github.com/developersteve/telstra-messaging-php)  ## SDK Repos   - [Messaging API - PHP SDK](https://github.com/telstra/MessagingAPI-SDK-php)   - [Messaging API - Python SDK](https://github.com/telstra/MessagingAPI-SDK-python)   - [Messaging API - Ruby SDK](https://github.com/telstra/MessagingAPI-SDK-ruby)   - [Messaging API - NodeJS SDK](https://github.com/telstra/MessagingAPI-SDK-node)   - [Messaging API - .Net2 SDK](https://github.com/telstra/MessagingAPI-SDK-dotnet)   - [Messaging API - Java SDK](https://github.com/telstra/MessagingAPI-SDK-Java)  ## Blog Posts For more information on the Messaging API, you can read these blog posts: - [Callbacks Part 1](https://dev.telstra.com/content/understanding-messaging-api-callbacks-part-1)  - [Callbacks Part 2](https://dev.telstra.com/content/understanding-messaging-api-callbacks-part-2)   # noqa: E501

    OpenAPI spec version: 2.2.9
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from Telstra_Messaging.api_client import ApiClient


class MessagingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_mms_status(self, messageid, **kwargs):  # noqa: E501
        """Get MMS Status  # noqa: E501

        Get MMS Status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mms_status(messageid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str messageid: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms  (required)
        :return: list[OutboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mms_status_with_http_info(messageid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mms_status_with_http_info(messageid, **kwargs)  # noqa: E501
            return data

    def get_mms_status_with_http_info(self, messageid, **kwargs):  # noqa: E501
        """Get MMS Status  # noqa: E501

        Get MMS Status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mms_status_with_http_info(messageid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str messageid: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms  (required)
        :return: list[OutboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['messageid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mms_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'messageid' is set
        if ('messageid' not in local_var_params or
                local_var_params['messageid'] is None):
            raise ValueError("Missing the required parameter `messageid` when calling `get_mms_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'messageid' in local_var_params:
            path_params['messageid'] = local_var_params['messageid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/mms/{messageid}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OutboundPollResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sms_status(self, message_id, **kwargs):  # noqa: E501
        """Get SMS Status  # noqa: E501

        If no notification URL has been specified, it is possible to poll for the message status. Note that the `MessageId` that appears in the URL must be URL encoded. Just copying the `MessageId` as it was supplied when submitting the message may not work.  SMS Status with Notification URL --- When a message has reached its final state, the API will send a POST to the URL that has been previously specified. <pre><code class=\"language-sh\">{     to: '+61418123456'     sentTimestamp: '2017-03-17T10:05:22+10:00'     receivedTimestamp: '2017-03-17T10:05:23+10:00'     messageId: /cccb284200035236000000000ee9d074019e0301/1261418123456     deliveryStatus: DELIVRD   } </code></pre>  The fields are: <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>to</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>deliveryStatus</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>messageId</code></td>       <td>The same reference that was returned when the original message was sent.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>   </tbody> </table>  Upon receiving this call it is expected that your servers will give a 204 (No Content) response. Anything else will cause the API to reattempt the call 5 minutes later.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sms_status(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms.  (required)
        :return: list[OutboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sms_status_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sms_status_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def get_sms_status_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Get SMS Status  # noqa: E501

        If no notification URL has been specified, it is possible to poll for the message status. Note that the `MessageId` that appears in the URL must be URL encoded. Just copying the `MessageId` as it was supplied when submitting the message may not work.  SMS Status with Notification URL --- When a message has reached its final state, the API will send a POST to the URL that has been previously specified. <pre><code class=\"language-sh\">{     to: '+61418123456'     sentTimestamp: '2017-03-17T10:05:22+10:00'     receivedTimestamp: '2017-03-17T10:05:23+10:00'     messageId: /cccb284200035236000000000ee9d074019e0301/1261418123456     deliveryStatus: DELIVRD   } </code></pre>  The fields are: <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>to</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>deliveryStatus</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>messageId</code></td>       <td>The same reference that was returned when the original message was sent.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>   </tbody> </table>  Upon receiving this call it is expected that your servers will give a 204 (No Content) response. Anything else will cause the API to reattempt the call 5 minutes later.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sms_status_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms.  (required)
        :return: list[OutboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sms_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in local_var_params or
                local_var_params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_sms_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'message_id' in local_var_params:
            path_params['messageId'] = local_var_params['message_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/sms/{messageId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OutboundPollResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_mms_responses(self, **kwargs):  # noqa: E501
        """Retrieve MMS Responses  # noqa: E501

        Messages are retrieved one at a time, starting with the earliest response. If the subscription has a `notifyURL`, response messages will be logged there instead.  # Notification URL Format for MMS Replies  <pre><code class=\"language-sh\">{   \"status\": \"RECEIVED\",   \"destinationAddress\": \"+61418123456\",   \"senderAddress\": \"+61421987654\",   \"subject\": \"Foo\",   \"sentTimestamp\": \"2018-03-23T12:15:45+10:00\",   \"envelope\": \"string\",   \"MMSContent\":     [       {         \"type\": \"text/plain\",         \"filename\": \"text_1.txt\",         \"payload\": \"string\"       },       {         \"type\": \"image/jpeg\",         \"filename\": \"sample.jpeg\",         \"payload\": \"string\"       }     ] }</code></pre>  The fields are: | Field | Description | | --- | --- | | `status` | The final state of the message. | | `destinationAddress` |The number the message was sent to. | | `senderAddress` | The number the message was sent from. | | `subject` | The subject assigned to the message. | | `sentTimestamp` | Time handling of the message ended. | | `envelope` | Information about about terminal type and originating operator. | | `MMSContent` | An array of the actual content of the reply message. | | `type` | The content type of the message. | | `filename` | The filename for the message content. | | `payload` | The content of the message. |   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_mms_responses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[MMSContent]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_mms_responses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_mms_responses_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_mms_responses_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve MMS Responses  # noqa: E501

        Messages are retrieved one at a time, starting with the earliest response. If the subscription has a `notifyURL`, response messages will be logged there instead.  # Notification URL Format for MMS Replies  <pre><code class=\"language-sh\">{   \"status\": \"RECEIVED\",   \"destinationAddress\": \"+61418123456\",   \"senderAddress\": \"+61421987654\",   \"subject\": \"Foo\",   \"sentTimestamp\": \"2018-03-23T12:15:45+10:00\",   \"envelope\": \"string\",   \"MMSContent\":     [       {         \"type\": \"text/plain\",         \"filename\": \"text_1.txt\",         \"payload\": \"string\"       },       {         \"type\": \"image/jpeg\",         \"filename\": \"sample.jpeg\",         \"payload\": \"string\"       }     ] }</code></pre>  The fields are: | Field | Description | | --- | --- | | `status` | The final state of the message. | | `destinationAddress` |The number the message was sent to. | | `senderAddress` | The number the message was sent from. | | `subject` | The subject assigned to the message. | | `sentTimestamp` | Time handling of the message ended. | | `envelope` | Information about about terminal type and originating operator. | | `MMSContent` | An array of the actual content of the reply message. | | `type` | The content type of the message. | | `filename` | The filename for the message content. | | `payload` | The content of the message. |   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_mms_responses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[MMSContent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_mms_responses" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/mms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MMSContent]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_sms_responses(self, **kwargs):  # noqa: E501
        """Retrieve SMS Responses  # noqa: E501

        Messages are retrieved one at a time, starting with the earliest response. The API supports the encoding of the full range of emojis in the reply message. The emojis will be in their UTF-8 format. If the subscription has a `notifyURL`, response messages will be logged there instead.  # Notification URL Format for SMS Response  <pre><code class=\"language-sh\">{   \"to\":\"+61472880123\",   \"from\":\"+61412345678\",   \"body\":\"Foo4\",   \"sentTimestamp\":\"2018-04-20T14:24:35\",   \"messageId\":\"DMASApiA0000000146\" }</code></pre>  The fields are: | Field | Description | | --- |--- | | `to` | The number the message was sent to. | | `from` | The number the message was sent from. | | `body` | The content of the SMS response. | | `sentTimestamp` | Time handling of the message ended. | | `messageId` | The ID assigned to the message. |   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_sms_responses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InboundPollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_sms_responses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_sms_responses_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_sms_responses_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve SMS Responses  # noqa: E501

        Messages are retrieved one at a time, starting with the earliest response. The API supports the encoding of the full range of emojis in the reply message. The emojis will be in their UTF-8 format. If the subscription has a `notifyURL`, response messages will be logged there instead.  # Notification URL Format for SMS Response  <pre><code class=\"language-sh\">{   \"to\":\"+61472880123\",   \"from\":\"+61412345678\",   \"body\":\"Foo4\",   \"sentTimestamp\":\"2018-04-20T14:24:35\",   \"messageId\":\"DMASApiA0000000146\" }</code></pre>  The fields are: | Field | Description | | --- |--- | | `to` | The number the message was sent to. | | `from` | The number the message was sent from. | | `body` | The content of the SMS response. | | `sentTimestamp` | Time handling of the message ended. | | `messageId` | The ID assigned to the message. |   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_sms_responses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InboundPollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_sms_responses" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/sms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InboundPollResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_mms(self, send_mms_request, **kwargs):  # noqa: E501
        """Send MMS  # noqa: E501

        Send MMS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_mms(send_mms_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendMmsRequest send_mms_request: A JSON or XML payload containing the recipient's phone number and MMS message.
The recipient number should be in the format '04xxxxxxxx' where x is a digit.
 (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_mms_with_http_info(send_mms_request, **kwargs)  # noqa: E501
        else:
            (data) = self.send_mms_with_http_info(send_mms_request, **kwargs)  # noqa: E501
            return data

    def send_mms_with_http_info(self, send_mms_request, **kwargs):  # noqa: E501
        """Send MMS  # noqa: E501

        Send MMS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_mms_with_http_info(send_mms_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendMmsRequest send_mms_request: A JSON or XML payload containing the recipient's phone number and MMS message.
The recipient number should be in the format '04xxxxxxxx' where x is a digit.
 (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['send_mms_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_mms" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'send_mms_request' is set
        if ('send_mms_request' not in local_var_params or
                local_var_params['send_mms_request'] is None):
            raise ValueError("Missing the required parameter `send_mms_request` when calling `send_mms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'send_mms_request' in local_var_params:
            body_params = local_var_params['send_mms_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/mms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageSentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_sms(self, send_sms_request, **kwargs):  # noqa: E501
        """Send SMS  # noqa: E501

        Send an SMS Message to a single or multiple mobile number/s.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_sms(send_sms_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendSMSRequest send_sms_request: A JSON or XML payload containing the recipient's phone number and text message.
This number can be in international format if preceeded by a '+' or in national format ('04xxxxxxxx') where x is a digit.
 (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_sms_with_http_info(send_sms_request, **kwargs)  # noqa: E501
        else:
            (data) = self.send_sms_with_http_info(send_sms_request, **kwargs)  # noqa: E501
            return data

    def send_sms_with_http_info(self, send_sms_request, **kwargs):  # noqa: E501
        """Send SMS  # noqa: E501

        Send an SMS Message to a single or multiple mobile number/s.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_sms_with_http_info(send_sms_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendSMSRequest send_sms_request: A JSON or XML payload containing the recipient's phone number and text message.
This number can be in international format if preceeded by a '+' or in national format ('04xxxxxxxx') where x is a digit.
 (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['send_sms_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_sms" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'send_sms_request' is set
        if ('send_sms_request' not in local_var_params or
                local_var_params['send_sms_request'] is None):
            raise ValueError("Missing the required parameter `send_sms_request` when calling `send_sms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'send_sms_request' in local_var_params:
            body_params = local_var_params['send_sms_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/sms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageSentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
