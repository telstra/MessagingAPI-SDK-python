# coding: utf-8

"""
    Telstra Messaging API

     # Introduction  Send and receive SMS and MMS messages globally using Telstraâ€™s enterprise grade Messaging API. It also allows your application to track the delivery status of both sent and received messages. Get your dedicated Australian number, and start sending and receiving messages today.  # Features  <p>The Telstra Messaging API provides the features below. <table>   <thead>     <tr>       <th>Feature</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>Dedicated Number</code></td>       <td>Provision a mobile number for your account to be used as from address in the API</td>     </tr>     <tr>       <td><code>Send Messages</code></td>       <td>Sending SMS or MMS messages</td>     </tr>     <tr>       <td><code>Receive Messages</code></td>       <td>Telstra will deliver messages sent to a dedicated number or to the <code>notifyURL</code> defined by you</td>     </tr>     <tr>       <td><code>Broadcast Messages</code></td>       <td>Invoke a single API to send a message to a list of number provided in <code>to</code></td>     </tr>     <tr>       <td><code>Delivery Status</code></td>       <td>Query the delivery status of your messages</td>     </tr>     <tr>       <td><code>Callbacks</code></td>       <td>Provide a notification URL and Telstra will notify your app when messages status changes</td>     </tr>     <tr>       <td><code>Alphanumeric Identifier</code></td>       <td>Differentiate yourself by providing an alphanumeric string in <code>from</code>. This feature is only available on paid plans</td>     </tr>     <tr>       <td><code>Concatenation</code></td>       <td>Send messages up to 1900 characters long and Telstra will automaticaly segment and reassemble them</td>     </tr>     <tr>       <td><code>Reply Request</code></td>       <td>Create a chat session by associating <code>messageId</code> and <code>to</code> number to track responses received from a mobile number. We will store this association for 8 days</td>     </tr>     <tr>       <td><code>Character set</code></td>       <td>Accepts all Unicode characters as part of UTF-8</td>     </tr>     <tr>       <td><code>Bounce-back response</code></td>       <td>See if your SMS hits an unreachable or unallocated number (Australia Only)</td>     </tr>     <tr>       <td><code>Queuing</code></td>       <td>Messaging API will automatically queue and deliver each message at a compliant rate.</td>     </tr>     <tr>       <td><code>Emoji Encoding</code></td>       <td>The API supports the encoding of the full range of emojis. Emojis in the reply messages will be in their UTF-8 format.</td>     </tr>   </tbody> </table>   # Getting Access to the API  <ol>   <li>Register at <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>.   <li>After registration, login to <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>        and navigate to the &quot;My apps&quot; page.    <li>Create your application by clicking the &quot;Add new app&quot; button    <li>Select &quot;API Free Trial&quot; Product when configuring your application. This Product includes the Telstra Messaging API as well as other APIs. Your application will be approved automatically.   <li>There is a maximum of 1000 free messages per developer. Additional messages and features can be purchased from <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>.   <li>Note your <code>Client key</code> and <code>Client secret</code> as these will be needed to provision a number for your application and for authentication. </ol>  <p>Now head over to <b>Getting Started</b> where you can find a postman collection as well as some links to sample apps and SDKs to get you started. <p>Happy Messaging!   # Getting Started  <p>Below are the steps to get started with the Telstra Messaging API.</p>    <ol>     <li>Generate OAuth2 Token using your <code>Client key</code> and <code>Client secret</code>.</li>     <li>Create Subscription in order to receive a provisioned number.</li>     <li>Send Message to a specific mobile number.</li>   </ol>    <h2>Run in Postman</h2>    <p><a   href=\"https://app.getpostman.com/run-collection/ded00578f69a9deba256#?env%5BMessaging%20API%20Environments%5D=W3siZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X2lkIiwidmFsdWUiOiIiLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X3NlY3JldCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6ImFjY2Vzc190b2tlbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Imhvc3QiLCJ2YWx1ZSI6InRhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiQXV0aG9yaXphdGlvbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Im9hdXRoX2hvc3QiLCJ2YWx1ZSI6InNhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoibWVzc2FnZV9pZCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifV0=\">   <img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\" /></a></p>    <h2>Sample Apps</h2>   - <a href=\"https://github.com/telstra/MessagingAPI-perl-sample-app\">Perl Sample App</a>   - <a href=\"https://github.com/telstra/messaging-sample-code-happy-chat\">Happy Chat App</a>   - <a href=\"https://github.com/developersteve/telstra-messaging-php\">PHP Sample App</a>    <h2>SDK repos</h2>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-php\">Messaging API - PHP SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-python\">Messaging API - Python SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-ruby\">Messaging API - Ruby SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-node\">Messaging API - NodeJS SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-dotnet\">Messaging API - .Net2 SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-Java\">Messaging API - Java SDK</a>  # Delivery Notification  The API provides several methods for notifying when a message has been delivered to the destination.  <ol>   <li>When you provision a number there is an opportunity to specify a <code>notifyURL</code>, when the message has been delivered the API will make a call to this URL to advise of the message status. If this is not provided then you can make use the Get Replies API to poll for messages.</li>   <li>If you do not specify a URL you can always call the <code>GET /sms</code> API get the latest replies to the message.</li> </ol>  <I>Please note that the notification URLs and the polling call are exclusive. If a notification URL has been set then the polling call will not provide any useful information.</I>  <h2>Notification URL Format</h2>  When a message has reached its final state, the API will send a POST to the URL that has been previously specified.   <h3>Notification URL Format for SMS</h3> <pre><code class=\"language-sh\">{     to: '+61418123456'     sentTimestamp: '2017-03-17T10:05:22+10:00'     receivedTimestamp: '2017-03-17T10:05:23+10:00'     messageId: /cccb284200035236000000000ee9d074019e0301/1261418123456     deliveryStatus: DELIVRD   } </code></pre> \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>to</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>deliveryStatus</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>messageId</code></td>       <td>The same reference that was returned when the original message was sent.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>   </tbody> </table>  Upon receiving this call it is expected that your servers will give a 204 (No Content) response. Anything else will cause the API to reattempt the call 5 minutes later.   <h3>Notification URL Format for SMS Replies</h3> <pre><code class=\"language-sh\">{     \"status\": \"RECEIVED\"     \"destinationAddress\": \"+61418123456\"     \"senderAddress\": \"+61421987654\"     \"message\": \"Foo\"             \"sentTimestamp\": \"2018-03-23T12:10:06+10:00\"   }                              </code></pre>  \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>status</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>destinationAddress</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>senderAddress</code></td>       <td>The number the message was sent from.</td>     </tr>     <tr>       <td><code>message</code></td>       <td>The sontent of the SMS reply.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>   </tbody> </table>  <h3>Notification URL Format for MMS Replies</h3> <pre><code class=\"language-sh\">{     \"status\": \"RECEIVED\",     \"destinationAddress\": \"+61418123456\",     \"senderAddress\": \"+61421987654\",     \"subject\": \"Foo\",     \"sentTimestamp\": \"2018-03-23T12:15:45+10:00\",     \"envelope\": \"string\",     \"MMSContent\":      [       {         \"type\": \"application/smil\",         \"filename\": \"smil.xml\",         \"payload\": \"string\"       },        {         \"type\": \"image/jpeg\",         \"filename\": \"sample.jpeg\",         \"payload\": \"string\"        }      ]    } </code></pre>  \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>status</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>destinationAddress</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>senderAddress</code></td>       <td>The number the message was sent from.</td>     </tr>     <tr>       <td><code>subject</code></td>       <td>The subject assigned to the message.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>envelope</code></td>       <td>Information about about terminal type and originating operator.</td>     </tr>     <tr>       <td><code>MMSContent</code></td>       <td>An array of the actual content of the reply message.</td>     </tr>     <tr>       <td><code>type</code></td>       <td>The content type of the message.</td>     </tr>     <tr>       <td><code>filename</code></td>       <td>The filename for the message content.</td>     </tr>     <tr>       <td><code>payload</code></td>       <td>The content of the message.</td>     </tr>   </tbody> </table>  # Frequently Asked Questions **Q: Can I send a broadcast message using the Telstra Messging API?** A. Yes. Recipient numbers can be in teh form of an array of strings if a broadcast message needs to be sent.  <h2>Notes</h2> <a href=\"http://petstore.swagger.io/?url=https://raw.githubusercontent.com/telstra/MessagingAPI-v2/master/docs/swagger/messaging-api-swagger.yaml\" target=\"_blank\">View messaging in Swagger UI</a>  # noqa: E501

    OpenAPI spec version: 2.2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from Telstra_Messaging.api_client import ApiClient


class MessagingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_mms_status(self, messageid, **kwargs):  # noqa: E501
        """Get MMS Status  # noqa: E501

        Get MMS Status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_mms_status(messageid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str messageid: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms (required)
        :return: list[OutboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_mms_status_with_http_info(messageid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mms_status_with_http_info(messageid, **kwargs)  # noqa: E501
            return data

    def get_mms_status_with_http_info(self, messageid, **kwargs):  # noqa: E501
        """Get MMS Status  # noqa: E501

        Get MMS Status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_mms_status_with_http_info(messageid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str messageid: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms (required)
        :return: list[OutboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['messageid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mms_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'messageid' is set
        if ('messageid' not in params or
                params['messageid'] is None):
            raise ValueError("Missing the required parameter `messageid` when calling `get_mms_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'messageid' in params:
            path_params['messageid'] = params['messageid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
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
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sms_status(self, message_id, **kwargs):  # noqa: E501
        """Get SMS Status  # noqa: E501

        If no notification URL has been specified, it is possible to poll for the message status. <pre><code class=\"language-sh\">  #!/bin/bash   #!/bin/bash   # Example of how to poll for a message status   AccessToken=\"Consumer Access Token\"   MessageId=\"Previous supplied Message Id, URL encoded\"   curl -X get -H \"Authorization: Bearer $AccessToken\" \\     -H \"Content-Type: application/json\" \\     \"https://tapi.telstra.com/v2/messages/sms/$MessageId\" </code></pre>  Note that the `MessageId` that appears in the URL must be URL encoded, just copying the `MessageId` as it was supplied when submitting the message may not work.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sms_status(message_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str message_id: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms. (required)
        :return: list[OutboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_sms_status_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sms_status_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def get_sms_status_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Get SMS Status  # noqa: E501

        If no notification URL has been specified, it is possible to poll for the message status. <pre><code class=\"language-sh\">  #!/bin/bash   #!/bin/bash   # Example of how to poll for a message status   AccessToken=\"Consumer Access Token\"   MessageId=\"Previous supplied Message Id, URL encoded\"   curl -X get -H \"Authorization: Bearer $AccessToken\" \\     -H \"Content-Type: application/json\" \\     \"https://tapi.telstra.com/v2/messages/sms/$MessageId\" </code></pre>  Note that the `MessageId` that appears in the URL must be URL encoded, just copying the `MessageId` as it was supplied when submitting the message may not work.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sms_status_with_http_info(message_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str message_id: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms. (required)
        :return: list[OutboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sms_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_sms_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
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
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_sms_responses(self, **kwargs):  # noqa: E501
        """Retrieve SMS Responses  # noqa: E501

        Messages are retrieved one at a time, starting with the earliest response. The API supports the encoding of the full range of emojis in the reply message. The emojis will be in their UTF-8 format. If the subscription has a `notifyURL`, response messages will be logged there instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_sms_responses(async=True)
        >>> result = thread.get()

        :param async bool
        :return: InboundPollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.retrieve_sms_responses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_sms_responses_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_sms_responses_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve SMS Responses  # noqa: E501

        Messages are retrieved one at a time, starting with the earliest response. The API supports the encoding of the full range of emojis in the reply message. The emojis will be in their UTF-8 format. If the subscription has a `notifyURL`, response messages will be logged there instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_sms_responses_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: InboundPollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_sms_responses" % key
                )
            params[key] = val
        del params['kwargs']

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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
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
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_mms(self, body, **kwargs):  # noqa: E501
        """Send MMS  # noqa: E501

        Send MMS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_mms(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendMmsRequest body: A JSON or XML payload containing the recipient's phone number and MMS message.The recipient number should be in the format '04xxxxxxxx' where x is a digit (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_mms_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_mms_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def send_mms_with_http_info(self, body, **kwargs):  # noqa: E501
        """Send MMS  # noqa: E501

        Send MMS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_mms_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendMmsRequest body: A JSON or XML payload containing the recipient's phone number and MMS message.The recipient number should be in the format '04xxxxxxxx' where x is a digit (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_mms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_mms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
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
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_sms(self, payload, **kwargs):  # noqa: E501
        """Send SMS  # noqa: E501

        Send an SMS Message to a single or multiple mobile number/s.  <h3>Send message to a single number: </h3> <pre><code class=\"language-sh\">  #!/bin/bash   # Use the Messaging API-v2 to send an SMS   # Note: only to: and body: are required   AccessToken=\"Access Token\"   Dest=\"Destination number\"   curl -X POST -H \"Authorization: Bearer $AccessToken\" -H \"Content-Type: application/json\" -d \"{     \\\"to\\\":\\\"$Dest\\\",     \\\"body\\\":\\\"Test Message\\\",     \\\"from\\\": \\\"+61412345678\\\",     \\\"validity\\\": 5,     \\\"scheduledDelivery\\\": 1,     \\\"notifyURL\\\": \\\"\\\",     \\\"replyRequest\\\": false     \\\"priority\\\": true   }\" \"https://tapi.telstra.com/v2/messages/sms\" </code></pre>  \\ <h3>Send message to multiple numbers: </h3> <pre><code class=\"language-sh\"> #!/bin/bash   # Use the Messaging API to send an SMS   AccessToken=\"Access Token\"   Dest=\"Destination number\"   curl -X post -H \"Authorization: Bearer $AccessToken\" \\     -H \"Content-Type: application/json\" \\     -d '{ \"to\":\"$dest1, $dest2, $dest3\", \"body\":\"Test Message\" }' \\     https://tapi.telstra.com/v2/messages/sms   <pre><code class=\"language-sh\">  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_sms(payload, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendSMSRequest payload: A JSON or XML payload containing the recipient's phone number and text message.  This number can be in international format if preceeded by a â€˜+â€™ or in national format ('04xxxxxxxx') where x is a digit. (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_sms_with_http_info(payload, **kwargs)  # noqa: E501
        else:
            (data) = self.send_sms_with_http_info(payload, **kwargs)  # noqa: E501
            return data

    def send_sms_with_http_info(self, payload, **kwargs):  # noqa: E501
        """Send SMS  # noqa: E501

        Send an SMS Message to a single or multiple mobile number/s.  <h3>Send message to a single number: </h3> <pre><code class=\"language-sh\">  #!/bin/bash   # Use the Messaging API-v2 to send an SMS   # Note: only to: and body: are required   AccessToken=\"Access Token\"   Dest=\"Destination number\"   curl -X POST -H \"Authorization: Bearer $AccessToken\" -H \"Content-Type: application/json\" -d \"{     \\\"to\\\":\\\"$Dest\\\",     \\\"body\\\":\\\"Test Message\\\",     \\\"from\\\": \\\"+61412345678\\\",     \\\"validity\\\": 5,     \\\"scheduledDelivery\\\": 1,     \\\"notifyURL\\\": \\\"\\\",     \\\"replyRequest\\\": false     \\\"priority\\\": true   }\" \"https://tapi.telstra.com/v2/messages/sms\" </code></pre>  \\ <h3>Send message to multiple numbers: </h3> <pre><code class=\"language-sh\"> #!/bin/bash   # Use the Messaging API to send an SMS   AccessToken=\"Access Token\"   Dest=\"Destination number\"   curl -X post -H \"Authorization: Bearer $AccessToken\" \\     -H \"Content-Type: application/json\" \\     -d '{ \"to\":\"$dest1, $dest2, $dest3\", \"body\":\"Test Message\" }' \\     https://tapi.telstra.com/v2/messages/sms   <pre><code class=\"language-sh\">  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_sms_with_http_info(payload, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendSMSRequest payload: A JSON or XML payload containing the recipient's phone number and text message.  This number can be in international format if preceeded by a â€˜+â€™ or in national format ('04xxxxxxxx') where x is a digit. (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payload']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payload' is set
        if ('payload' not in params or
                params['payload'] is None):
            raise ValueError("Missing the required parameter `payload` when calling `send_sms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
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
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
