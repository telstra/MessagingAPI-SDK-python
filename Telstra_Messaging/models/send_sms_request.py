# coding: utf-8

"""
    Telstra Messaging API

     # Introduction  Send and receive SMS and MMS messages globally using Telstraâ€™s enterprise grade Messaging API. It also allows your application to track the delivery status of both sent and received messages. Get your dedicated Australian number, and start sending and receiving messages today.  # Features  <p>The Telstra Messaging API provides the features below. <table>   <thead>     <tr>       <th>Feature</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>Dedicated Number</code></td>       <td>Provision a mobile number for your account to be used as from address in the API</td>     </tr>     <tr>       <td><code>Send Messages</code></td>       <td>Sending SMS or MMS messages</td>     </tr>     <tr>       <td><code>Receive Messages</code></td>       <td>Telstra will deliver messages sent to a dedicated number or to the <code>notifyURL</code> defined by you</td>     </tr>     <tr>       <td><code>Broadcast Messages</code></td>       <td>Invoke a single API to send a message to a list of number provided in <code>to</code></td>     </tr>     <tr>       <td><code>Delivery Status</code></td>       <td>Query the delivery status of your messages</td>     </tr>     <tr>       <td><code>Callbacks</code></td>       <td>Provide a notification URL and Telstra will notify your app when messages status changes</td>     </tr>     <tr>       <td><code>Alphanumeric Identifier</code></td>       <td>Differentiate yourself by providing an alphanumeric string in <code>from</code>. This feature is only available on paid plans</td>     </tr>     <tr>       <td><code>Concatenation</code></td>       <td>Send messages up to 1900 characters long and Telstra will automaticaly segment and reassemble them</td>     </tr>     <tr>       <td><code>Reply Request</code></td>       <td>Create a chat session by associating <code>messageId</code> and <code>to</code> number to track responses received from a mobile number. We will store this association for 8 days</td>     </tr>     <tr>       <td><code>Character set</code></td>       <td>Accepts all Unicode characters as part of UTF-8</td>     </tr>     <tr>       <td><code>Bounce-back response</code></td>       <td>See if your SMS hits an unreachable or unallocated number (Australia Only)</td>     </tr>     <tr>       <td><code>Queuing</code></td>       <td>Messaging API will automatically queue and deliver each message at a compliant rate.</td>     </tr>     <tr>       <td><code>Emoji Encoding</code></td>       <td>The API supports the encoding of the full range of emojis. Emojis in the reply messages will be in their UTF-8 format.</td>     </tr>   </tbody> </table>   # Getting Access to the API  <ol>   <li>Register at <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>.   <li>After registration, login to <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>        and navigate to the &quot;My apps&quot; page.    <li>Create your application by clicking the &quot;Add new app&quot; button    <li>Select &quot;API Free Trial&quot; Product when configuring your application. This Product includes the Telstra Messaging API as well as other APIs. Your application will be approved automatically.   <li>There is a maximum of 1000 free messages per developer. Additional messages and features can be purchased from <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>.   <li>Note your <code>Client key</code> and <code>Client secret</code> as these will be needed to provision a number for your application and for authentication. </ol>  <p>Now head over to <b>Getting Started</b> where you can find a postman collection as well as some links to sample apps and SDKs to get you started. <p>Happy Messaging!   # Getting Started  <p>Below are the steps to get started with the Telstra Messaging API.</p>    <ol>     <li>Generate OAuth2 Token using your <code>Client key</code> and <code>Client secret</code>.</li>     <li>Create Subscription in order to receive a provisioned number.</li>     <li>Send Message to a specific mobile number.</li>   </ol>    <h2>Run in Postman</h2>    <p><a   href=\"https://app.getpostman.com/run-collection/ded00578f69a9deba256#?env%5BMessaging%20API%20Environments%5D=W3siZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X2lkIiwidmFsdWUiOiIiLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X3NlY3JldCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6ImFjY2Vzc190b2tlbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Imhvc3QiLCJ2YWx1ZSI6InRhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiQXV0aG9yaXphdGlvbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Im9hdXRoX2hvc3QiLCJ2YWx1ZSI6InNhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoibWVzc2FnZV9pZCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifV0=\">   <img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\" /></a></p>    <h2>Sample Apps</h2>   - <a href=\"https://github.com/telstra/MessagingAPI-perl-sample-app\">Perl Sample App</a>   - <a href=\"https://github.com/telstra/messaging-sample-code-happy-chat\">Happy Chat App</a>   - <a href=\"https://github.com/developersteve/telstra-messaging-php\">PHP Sample App</a>    <h2>SDK repos</h2>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-php\">Messaging API - PHP SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-python\">Messaging API - Python SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-ruby\">Messaging API - Ruby SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-node\">Messaging API - NodeJS SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-dotnet\">Messaging API - .Net2 SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-Java\">Messaging API - Java SDK</a>  # Delivery Notification  The API provides several methods for notifying when a message has been delivered to the destination.  <ol>   <li>When you provision a number there is an opportunity to specify a <code>notifyURL</code>, when the message has been delivered the API will make a call to this URL to advise of the message status. If this is not provided then you can make use the Get Replies API to poll for messages.</li>   <li>If you do not specify a URL you can always call the <code>GET /sms</code> API get the latest replies to the message.</li> </ol>  <I>Please note that the notification URLs and the polling call are exclusive. If a notification URL has been set then the polling call will not provide any useful information.</I>  <h2>Notification URL Format</h2>  When a message has reached its final state, the API will send a POST to the URL that has been previously specified.   <h3>Notification URL Format for SMS</h3> <pre><code class=\"language-sh\">{     to: '+61418123456'     sentTimestamp: '2017-03-17T10:05:22+10:00'     receivedTimestamp: '2017-03-17T10:05:23+10:00'     messageId: /cccb284200035236000000000ee9d074019e0301/1261418123456     deliveryStatus: DELIVRD   } </code></pre> \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>to</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>deliveryStatus</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>messageId</code></td>       <td>The same reference that was returned when the original message was sent.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>   </tbody> </table>  Upon receiving this call it is expected that your servers will give a 204 (No Content) response. Anything else will cause the API to reattempt the call 5 minutes later.   <h3>Notification URL Format for SMS Replies</h3> <pre><code class=\"language-sh\">{     \"status\": \"RECEIVED\"     \"destinationAddress\": \"+61418123456\"     \"senderAddress\": \"+61421987654\"     \"message\": \"Foo\"             \"sentTimestamp\": \"2018-03-23T12:10:06+10:00\"   }                              </code></pre>  \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>status</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>destinationAddress</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>senderAddress</code></td>       <td>The number the message was sent from.</td>     </tr>     <tr>       <td><code>message</code></td>       <td>The sontent of the SMS reply.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>   </tbody> </table>  <h3>Notification URL Format for MMS Replies</h3> <pre><code class=\"language-sh\">{     \"status\": \"RECEIVED\",     \"destinationAddress\": \"+61418123456\",     \"senderAddress\": \"+61421987654\",     \"subject\": \"Foo\",     \"sentTimestamp\": \"2018-03-23T12:15:45+10:00\",     \"envelope\": \"string\",     \"MMSContent\":      [       {         \"type\": \"application/smil\",         \"filename\": \"smil.xml\",         \"payload\": \"string\"       },        {         \"type\": \"image/jpeg\",         \"filename\": \"sample.jpeg\",         \"payload\": \"string\"        }      ]    } </code></pre>  \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>status</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>destinationAddress</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>senderAddress</code></td>       <td>The number the message was sent from.</td>     </tr>     <tr>       <td><code>subject</code></td>       <td>The subject assigned to the message.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>envelope</code></td>       <td>Information about about terminal type and originating operator.</td>     </tr>     <tr>       <td><code>MMSContent</code></td>       <td>An array of the actual content of the reply message.</td>     </tr>     <tr>       <td><code>type</code></td>       <td>The content type of the message.</td>     </tr>     <tr>       <td><code>filename</code></td>       <td>The filename for the message content.</td>     </tr>     <tr>       <td><code>payload</code></td>       <td>The content of the message.</td>     </tr>   </tbody> </table>  # Frequently Asked Questions **Q: Can I send a broadcast message using the Telstra Messging API?** A. Yes. Recipient numbers can be in teh form of an array of strings if a broadcast message needs to be sent.  <h2>Notes</h2> <a href=\"http://petstore.swagger.io/?url=https://raw.githubusercontent.com/telstra/MessagingAPI-v2/master/docs/swagger/messaging-api-swagger.yaml\" target=\"_blank\">View messaging in Swagger UI</a>  # noqa: E501

    OpenAPI spec version: 2.2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SendSMSRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'to': 'str',
        'body': 'str',
        '_from': 'str',
        'validity': 'int',
        'scheduled_delivery': 'int',
        'notify_url': 'str',
        'reply_request': 'bool',
        'priority': 'bool'
    }

    attribute_map = {
        'to': 'to',
        'body': 'body',
        '_from': 'from',
        'validity': 'validity',
        'scheduled_delivery': 'scheduledDelivery',
        'notify_url': 'notifyURL',
        'reply_request': 'replyRequest',
        'priority': 'priority'
    }

    def __init__(self, to=None, body=None, _from=None, validity=None, scheduled_delivery=None, notify_url=None, reply_request=None, priority=None):  # noqa: E501
        """SendSMSRequest - a model defined in Swagger"""  # noqa: E501

        self._to = None
        self._body = None
        self.__from = None
        self._validity = None
        self._scheduled_delivery = None
        self._notify_url = None
        self._reply_request = None
        self._priority = None
        self.discriminator = None

        self.to = to
        self.body = body
        if _from is not None:
            self._from = _from
        if validity is not None:
            self.validity = validity
        if scheduled_delivery is not None:
            self.scheduled_delivery = scheduled_delivery
        if notify_url is not None:
            self.notify_url = notify_url
        if reply_request is not None:
            self.reply_request = reply_request
        if priority is not None:
            self.priority = priority

    @property
    def to(self):
        """Gets the to of this SendSMSRequest.  # noqa: E501

        Phone number (in E.164 format) to send the SMS to.  This number can be in international format `\"to\": \"+61412345678\"` or in national format. Can be an array of strings if sending to multiple numbers: `\"to\": \"+61412345678, +61418765432\"`  # noqa: E501

        :return: The to of this SendSMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendSMSRequest.

        Phone number (in E.164 format) to send the SMS to.  This number can be in international format `\"to\": \"+61412345678\"` or in national format. Can be an array of strings if sending to multiple numbers: `\"to\": \"+61412345678, +61418765432\"`  # noqa: E501

        :param to: The to of this SendSMSRequest.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def body(self):
        """Gets the body of this SendSMSRequest.  # noqa: E501

        The text body of the message. Messages longer than 160 characters will be counted as multiple messages. This field contains the message text, this can be up to 1900 (for a single recipient) or 500 (for multiple recipients) UTF-8 characters. As mobile devices rarely support the full range of UTF-8 characters, it is possible that some characters may not be translated correctly by the mobile device  # noqa: E501

        :return: The body of this SendSMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SendSMSRequest.

        The text body of the message. Messages longer than 160 characters will be counted as multiple messages. This field contains the message text, this can be up to 1900 (for a single recipient) or 500 (for multiple recipients) UTF-8 characters. As mobile devices rarely support the full range of UTF-8 characters, it is possible that some characters may not be translated correctly by the mobile device  # noqa: E501

        :param body: The body of this SendSMSRequest.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def _from(self):
        """Gets the _from of this SendSMSRequest.  # noqa: E501

        The Alphanumeric sender ID of up to 11 characters or phone number the SMS was sent from. If not present, the service will use the mobile number associated with the application (in E.164 format). This feature is only available on paid plans.  # noqa: E501

        :return: The _from of this SendSMSRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendSMSRequest.

        The Alphanumeric sender ID of up to 11 characters or phone number the SMS was sent from. If not present, the service will use the mobile number associated with the application (in E.164 format). This feature is only available on paid plans.  # noqa: E501

        :param _from: The _from of this SendSMSRequest.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def validity(self):
        """Gets the validity of this SendSMSRequest.  # noqa: E501

        How long the platform should attempt to deliver the message for. This period is specified in minutes from the message. Normally if the message cannot be delivered immediately, it will be stored and delivery will be periodically reattempted. The network will attempt to send the message for up to seven days. It is possible to define a period smaller than 7 days by including this parameter and specifying the number of minutes that delivery should be attempted. eg: including `\"validity\": 60` will specify that if a message can't be delivered within the first 60 minutes them the network should stop.  # noqa: E501

        :return: The validity of this SendSMSRequest.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this SendSMSRequest.

        How long the platform should attempt to deliver the message for. This period is specified in minutes from the message. Normally if the message cannot be delivered immediately, it will be stored and delivery will be periodically reattempted. The network will attempt to send the message for up to seven days. It is possible to define a period smaller than 7 days by including this parameter and specifying the number of minutes that delivery should be attempted. eg: including `\"validity\": 60` will specify that if a message can't be delivered within the first 60 minutes them the network should stop.  # noqa: E501

        :param validity: The validity of this SendSMSRequest.  # noqa: E501
        :type: int
        """

        self._validity = validity

    @property
    def scheduled_delivery(self):
        """Gets the scheduled_delivery of this SendSMSRequest.  # noqa: E501

        How long the platform should wait before attempting to send the message - specified in minutes. e.g.: If `\"scheduledDelivery\": 120` is included, then the network will not attempt to start message delivery for two hours after the message has been submitted  # noqa: E501

        :return: The scheduled_delivery of this SendSMSRequest.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_delivery

    @scheduled_delivery.setter
    def scheduled_delivery(self, scheduled_delivery):
        """Sets the scheduled_delivery of this SendSMSRequest.

        How long the platform should wait before attempting to send the message - specified in minutes. e.g.: If `\"scheduledDelivery\": 120` is included, then the network will not attempt to start message delivery for two hours after the message has been submitted  # noqa: E501

        :param scheduled_delivery: The scheduled_delivery of this SendSMSRequest.  # noqa: E501
        :type: int
        """

        self._scheduled_delivery = scheduled_delivery

    @property
    def notify_url(self):
        """Gets the notify_url of this SendSMSRequest.  # noqa: E501

        Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc. It is possible for the network to make a call to a URL when the message has been delivered (or has expired), different URLs can be set per message. Please refer to the Delivery Notification section.  # noqa: E501

        :return: The notify_url of this SendSMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this SendSMSRequest.

        Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc. It is possible for the network to make a call to a URL when the message has been delivered (or has expired), different URLs can be set per message. Please refer to the Delivery Notification section.  # noqa: E501

        :param notify_url: The notify_url of this SendSMSRequest.  # noqa: E501
        :type: str
        """

        self._notify_url = notify_url

    @property
    def reply_request(self):
        """Gets the reply_request of this SendSMSRequest.  # noqa: E501

        If set to true, the reply message functionality will be implemented and the to address will be ignored if present. If false or not present, then normal message handling is implemented. When set to true, network will use a temporary number to deliver this message. All messages sent by mobile to this temporary number will be stored against the same `messageId`. If a `notifyURL` is provided then user response will be delivered to the URL where `messageId` will be same as `messageId` in reponse to original API request. This field contains the message text, this can be up to 500 UTF-8 characters. As mobile devices rarely support the full range of UTF-8 characters, it is possible that some characters may not be translated correctly by the mobile device.  # noqa: E501

        :return: The reply_request of this SendSMSRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reply_request

    @reply_request.setter
    def reply_request(self, reply_request):
        """Sets the reply_request of this SendSMSRequest.

        If set to true, the reply message functionality will be implemented and the to address will be ignored if present. If false or not present, then normal message handling is implemented. When set to true, network will use a temporary number to deliver this message. All messages sent by mobile to this temporary number will be stored against the same `messageId`. If a `notifyURL` is provided then user response will be delivered to the URL where `messageId` will be same as `messageId` in reponse to original API request. This field contains the message text, this can be up to 500 UTF-8 characters. As mobile devices rarely support the full range of UTF-8 characters, it is possible that some characters may not be translated correctly by the mobile device.  # noqa: E501

        :param reply_request: The reply_request of this SendSMSRequest.  # noqa: E501
        :type: bool
        """

        self._reply_request = reply_request

    @property
    def priority(self):
        """Gets the priority of this SendSMSRequest.  # noqa: E501

        When messages are queued up for a number, then it is possible to set where a new message will be placed in the queue. If the priority is set to true then the new message will be placed ahead of all messages with a normal priority. If there are no messages queued for the number, then this parameter has no effect.  # noqa: E501

        :return: The priority of this SendSMSRequest.  # noqa: E501
        :rtype: bool
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this SendSMSRequest.

        When messages are queued up for a number, then it is possible to set where a new message will be placed in the queue. If the priority is set to true then the new message will be placed ahead of all messages with a normal priority. If there are no messages queued for the number, then this parameter has no effect.  # noqa: E501

        :param priority: The priority of this SendSMSRequest.  # noqa: E501
        :type: bool
        """

        self._priority = priority

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendSMSRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
