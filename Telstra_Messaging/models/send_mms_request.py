# coding: utf-8

"""
    Telstra Messaging API

     # Introduction  Send and receive SMS and MMS messages globally using Telstraâ€™s enterprise grade Messaging API. It also allows your application to track the delivery status of both sent and received messages. Get your dedicated Australian number, and start sending and receiving messages today.  # Features  The Telstra Messaging API provides the features below. | Feature | Description | | --- | --- | | `Dedicated Number` | Provision a mobile number for your account to be used as `from` address in the API | | `Send Messages` | Sending SMS or MMS messages | | `Receive Messages` | Telstra will deliver messages sent to a dedicated number or to the `notifyURL` defined by you | | `Broadcast Messages` | Invoke a single API call to send a message to a list of numbers provided in `to` | | `Delivery Status` | Query the delivery status of your messages | | `Callbacks` | Provide a notification URL and Telstra will notify your app when a message status changes | | `Alphanumeric Identifier` | Differentiate yourself by providing an alphanumeric string in `from`. This feature is only available on paid plans | | `Concatenation` | Send messages up to 1900 characters long and Telstra will automaticaly segment and reassemble them | | `Reply Request` | Create a chat session by associating `messageId` and `to` number to track responses received from a mobile number. We will store this association for 8 days | | `Character set` | Accepts all Unicode characters as part of UTF-8 | | `Bounce-back response` | See if your SMS hits an unreachable or unallocated number (Australia Only) | | `Queuing` | Messaging API will automatically queue and deliver each message at a compliant rate. | | `Emoji Encoding` | The API supports the encoding of the full range of emojis. Emojis in the reply messages will be in their UTF-8 format. |  ## Delivery Notification or Callbacks  The API provides several methods for notifying when a message has been delivered to the destination.  1. When you send a message there is an opportunity to specify a `notifyURL`. Once the message has been delivered the API will make a call to this URL to advise of the message status. 2. If you do not specify a URL you can always call the `GET /status` API to get the status of the message.  # Getting Access to the API  1. Register at [https://dev.telstra.com](https://dev.telstra.com). 2. After registration, login to [https://dev.telstra.com](https://dev.telstra.com) and navigate to the **My apps** page. 3. Create your application by clicking the **Add new app** button 4. Select **API Free Trial** Product when configuring your application. This Product includes the Telstra Messaging API as well as other free trial APIs. Your application will be approved automatically. 5. There is a maximum of 1000 free messages per developer. Additional messages and features can be purchased from [https://dev.telstra.com](https://dev.telstra.com). 6. Note your `Client key` and `Client secret` as these will be needed to provision a number for your application and for authentication.  Now head over to **Getting Started** where you can find a postman collection as well as some links to sample apps and SDKs to get you started. Happy Messaging!  # Frequently Asked Questions  **Q: Is creating a subscription via the Provisioning call a required step?** A. Yes. You will only be able to start sending messages if you have a provisioned dedicated number. Use Provisioning to create a dedicated number subscription, or renew your dedicated number if it has expired.  **Q: When trying to send an SMS I receive a `400 Bad Request` response. How can I fix this?** A. You need to make sure you have a provisioned dedicated number before you can send an SMS.  If you do not have a provisioned dedicated number and you try to send a message via the API, you will get the error below in the response:  <pre><code class=\"language-sh\">{   \"status\":\"400\",   \"code\":\"DELIVERY-IMPOSSIBLE\",   \"message\":\"Invalid \\'from\\' address specified\" }</code></pre>  Use Provisioning to create a dedicated number subscription, or renew your dedicated number if it has expired.  **Q: How long does my dedicated number stay active for?** A. When you provision a dedicated number, by default it will be active for 30-days. You can use the `activeDays` parameter during the provisioning call to increment or decrement the number of days your dedicated number will remain active.  **Q: Can I send a broadcast message using the Telstra Messaging API?** A. Yes. Recipient numbers can be in the form of an array of strings if a broadcast message needs to be sent, allowing you to send to multiple mobile numbers in one API call.   A sample request body for this will be: `{\"to\":[\"+61412345678\",\"+61487654321\"],\"body\":\"Test Message\"}`  **Q: Can I use `Alphanumeric Identifier` from my paid plan via credit card?** A. `Alphanumeric Identifier` is only available on Telstra Account paid plans, not through credit card paid plans.  **Q: What is the maximum sized MMS that I can send?** A. This will depend on the carrier that will receive the MMS. For Telstra it's up to 2MB,  Optus up to 1.5MB and Vodafone only allows up to 500kB. You will need to check with international carriers for thier MMS size limits.  **Q: How is the size of an MMS calculated?** A. Images are scaled up to approximately 4/3 when base64 encoded. Additionally, there is approximately 200 bytes of overhead on each MMS. Assuming the maximum MMS that can be sent on Telstraâ€™s network is 2MB, then the maximum image size that can be sent will be approximately 1.378MB (1.378 x 1.34 + 200, without SOAP encapsulation).  **Q: How is an MMS classified as Small or Large?** A. MMSes with size below 600kB are classed as Small whereas those that are bigger than 600kB are classed as Large. They will be charged accordingly.  **Q: Are SMILs supported by the Messaging API?** A. While there will be no error if you send an MMS with a SMIL presentation, the actual layout or sequence defined in the SMIL may not display as expected because most of the new smartphone devices ignore the SMIL presentation layer. SMIL was used in feature phones which had limited capability and SMIL allowed a *powerpoint type* presentation to be provided. Smartphones now have the capability to display video which is the better option for presentations. It is recommended that MMS messages should just drop the SMIL.  **Q: How do I assign a delivery notification or callback URL?** A. You can assign a delivery notification or callback URL by adding the `notifyURL` parameter in the body of the request when you send a message. Once the message has been delivered, a notification will then be posted to this callback URL.  **Q: What is the difference between the `notifyURL` parameter in the Provisoning call versus the `notifyURL` parameter in the Send Message call?** A. The `notifyURL` in the Provisoning call will be the URL where replies to the provisioned number will be posted. On the other hand, the `notifyURL` in the Send Message call will be the URL where the delivery notification will be posted, e.g. when an SMS has already been delivered to the recipient.  # Getting Started  Below are the steps to get started with the Telstra Messaging API.   1. Generate an OAuth2 token using your `Client key` and `Client secret`.   2. Use the Provisioning call to create a subscription and receive a dedicated number.   3. Send a message to a specific mobile number.  ## Run in Postman <a href=\"https://app.getpostman.com/run-collection/ded00578f69a9deba256#?env%5BMessaging%20API%20Environments%5D=W3siZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X2lkIiwidmFsdWUiOiIiLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X3NlY3JldCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6ImFjY2Vzc190b2tlbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Imhvc3QiLCJ2YWx1ZSI6InRhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiQXV0aG9yaXphdGlvbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Im9hdXRoX2hvc3QiLCJ2YWx1ZSI6InNhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoibWVzc2FnZV9pZCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifV0=\"><img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\"/></a>  ## Sample Apps   - [Perl Sample App](https://github.com/telstra/MessagingAPI-perl-sample-app)   - [Happy Chat App](https://github.com/telstra/messaging-sample-code-happy-chat)   - [PHP Sample App](https://github.com/developersteve/telstra-messaging-php)  ## SDK Repos   - [Messaging API - PHP SDK](https://github.com/telstra/MessagingAPI-SDK-php)   - [Messaging API - Python SDK](https://github.com/telstra/MessagingAPI-SDK-python)   - [Messaging API - Ruby SDK](https://github.com/telstra/MessagingAPI-SDK-ruby)   - [Messaging API - NodeJS SDK](https://github.com/telstra/MessagingAPI-SDK-node)   - [Messaging API - .Net2 SDK](https://github.com/telstra/MessagingAPI-SDK-dotnet)   - [Messaging API - Java SDK](https://github.com/telstra/MessagingAPI-SDK-Java)  ## Blog Posts For more information on the Messaging API, you can read these blog posts: - [Callbacks Part 1](https://dev.telstra.com/content/understanding-messaging-api-callbacks-part-1)  - [Callbacks Part 2](https://dev.telstra.com/content/understanding-messaging-api-callbacks-part-2)   # noqa: E501

    OpenAPI spec version: 2.2.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SendMmsRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        '_from': 'str',
        'to': 'str',
        'subject': 'str',
        'reply_request': 'bool',
        'notify_url': 'str',
        'mms_content': 'list[MMSContent]'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'subject': 'subject',
        'reply_request': 'replyRequest',
        'notify_url': 'notifyURL',
        'mms_content': 'MMSContent'
    }

    def __init__(self, _from=None, to=None, subject=None, reply_request=None, notify_url=None, mms_content=None):  # noqa: E501
        """SendMmsRequest - a model defined in OpenAPI"""  # noqa: E501

        self.__from = None
        self._to = None
        self._subject = None
        self._reply_request = None
        self._notify_url = None
        self._mms_content = None
        self.discriminator = None

        self._from = _from
        self.to = to
        self.subject = subject
        self.reply_request = reply_request
        if notify_url is not None:
            self.notify_url = notify_url
        self.mms_content = mms_content

    @property
    def _from(self):
        """Gets the _from of this SendMmsRequest.  # noqa: E501

        This will be the source address that will be displayed on the receiving device. If it is not present then it will default to the MSISDN assigned to the app. If replyRequest is set to true, then this field will be ignored.   # noqa: E501

        :return: The _from of this SendMmsRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendMmsRequest.

        This will be the source address that will be displayed on the receiving device. If it is not present then it will default to the MSISDN assigned to the app. If replyRequest is set to true, then this field will be ignored.   # noqa: E501

        :param _from: The _from of this SendMmsRequest.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this SendMmsRequest.  # noqa: E501

        This is the destination address. Can be an array of strings if sending to multiple numbers: \"to\":[\"+61412345678\", \"+61418765432\"]   # noqa: E501

        :return: The to of this SendMmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendMmsRequest.

        This is the destination address. Can be an array of strings if sending to multiple numbers: \"to\":[\"+61412345678\", \"+61418765432\"]   # noqa: E501

        :param to: The to of this SendMmsRequest.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def subject(self):
        """Gets the subject of this SendMmsRequest.  # noqa: E501

        The subject that will be used in an MMS message.  # noqa: E501

        :return: The subject of this SendMmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SendMmsRequest.

        The subject that will be used in an MMS message.  # noqa: E501

        :param subject: The subject of this SendMmsRequest.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def reply_request(self):
        """Gets the reply_request of this SendMmsRequest.  # noqa: E501

        If set to true, the reply message functionality will be implemented and the to address will be ignored if present.  # noqa: E501

        :return: The reply_request of this SendMmsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reply_request

    @reply_request.setter
    def reply_request(self, reply_request):
        """Sets the reply_request of this SendMmsRequest.

        If set to true, the reply message functionality will be implemented and the to address will be ignored if present.  # noqa: E501

        :param reply_request: The reply_request of this SendMmsRequest.  # noqa: E501
        :type: bool
        """
        if reply_request is None:
            raise ValueError("Invalid value for `reply_request`, must not be `None`")  # noqa: E501

        self._reply_request = reply_request

    @property
    def notify_url(self):
        """Gets the notify_url of this SendMmsRequest.  # noqa: E501

        Notify url  # noqa: E501

        :return: The notify_url of this SendMmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this SendMmsRequest.

        Notify url  # noqa: E501

        :param notify_url: The notify_url of this SendMmsRequest.  # noqa: E501
        :type: str
        """

        self._notify_url = notify_url

    @property
    def mms_content(self):
        """Gets the mms_content of this SendMmsRequest.  # noqa: E501

        An array of content that will be sent in an MMS message. If this array is present it will cause the `body` element to be ignored, and the message will be sent as an MMS.  # noqa: E501

        :return: The mms_content of this SendMmsRequest.  # noqa: E501
        :rtype: list[MMSContent]
        """
        return self._mms_content

    @mms_content.setter
    def mms_content(self, mms_content):
        """Sets the mms_content of this SendMmsRequest.

        An array of content that will be sent in an MMS message. If this array is present it will cause the `body` element to be ignored, and the message will be sent as an MMS.  # noqa: E501

        :param mms_content: The mms_content of this SendMmsRequest.  # noqa: E501
        :type: list[MMSContent]
        """
        if mms_content is None:
            raise ValueError("Invalid value for `mms_content`, must not be `None`")  # noqa: E501

        self._mms_content = mms_content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, SendMmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
