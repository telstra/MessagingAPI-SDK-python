# coding: utf-8

"""
    Telstra Messaging API

     # Introduction  Send and receive SMS and MMS messages globally using Telstraâ€™s enterprise grade Messaging API. It also allows your application to track the delivery status of both sent and received messages. Get your dedicated Australian number, and start sending and receiving messages today.  # Features  <p>The Telstra Messaging API provides the features below. <table>   <thead>     <tr>       <th>Feature</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>Dedicated Number</code></td>       <td>Provision a mobile number for your account to be used as from address in the API</td>     </tr>     <tr>       <td><code>Send Messages</code></td>       <td>Sending SMS or MMS messages</td>     </tr>     <tr>       <td><code>Receive Messages</code></td>       <td>Telstra will deliver messages sent to a dedicated number or to the <code>notifyURL</code> defined by you</td>     </tr>     <tr>       <td><code>Broadcast Messages</code></td>       <td>Invoke a single API to send a message to a list of number provided in <code>to</code></td>     </tr>     <tr>       <td><code>Delivery Status</code></td>       <td>Query the delivery status of your messages</td>     </tr>     <tr>       <td><code>Callbacks</code></td>       <td>Provide a notification URL and Telstra will notify your app when messages status changes</td>     </tr>     <tr>       <td><code>Alphanumeric Identifier</code></td>       <td>Differentiate yourself by providing an alphanumeric string in <code>from</code>. This feature is only available on paid plans</td>     </tr>     <tr>       <td><code>Concatenation</code></td>       <td>Send messages up to 1900 characters long and Telstra will automaticaly segment and reassemble them</td>     </tr>     <tr>       <td><code>Reply Request</code></td>       <td>Create a chat session by associating <code>messageId</code> and <code>to</code> number to track responses received from a mobile number. We will store this association for 8 days</td>     </tr>     <tr>       <td><code>Character set</code></td>       <td>Accepts all Unicode characters as part of UTF-8</td>     </tr>     <tr>       <td><code>Bounce-back response</code></td>       <td>See if your SMS hits an unreachable or unallocated number (Australia Only)</td>     </tr>     <tr>       <td><code>Queuing</code></td>       <td>Messaging API will automatically queue and deliver each message at a compliant rate.</td>     </tr>     <tr>       <td><code>Emoji Encoding</code></td>       <td>The API supports the encoding of the full range of emojis. Emojis in the reply messages will be in their UTF-8 format.</td>     </tr>   </tbody> </table>   # Getting Access to the API  <ol>   <li>Register at <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>.   <li>After registration, login to <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>        and navigate to the &quot;My apps&quot; page.    <li>Create your application by clicking the &quot;Add new app&quot; button    <li>Select &quot;API Free Trial&quot; Product when configuring your application. This Product includes the Telstra Messaging API as well as other APIs. Your application will be approved automatically.   <li>There is a maximum of 1000 free messages per developer. Additional messages and features can be purchased from <a href=\"https://dev.telstra.com\">https://dev.telstra.com</a>.   <li>Note your <code>Client key</code> and <code>Client secret</code> as these will be needed to provision a number for your application and for authentication. </ol>  <p>Now head over to <b>Getting Started</b> where you can find a postman collection as well as some links to sample apps and SDKs to get you started. <p>Happy Messaging!   # Getting Started  <p>Below are the steps to get started with the Telstra Messaging API.</p>    <ol>     <li>Generate OAuth2 Token using your <code>Client key</code> and <code>Client secret</code>.</li>     <li>Create Subscription in order to receive a provisioned number.</li>     <li>Send Message to a specific mobile number.</li>   </ol>    <h2>Run in Postman</h2>    <p><a   href=\"https://app.getpostman.com/run-collection/ded00578f69a9deba256#?env%5BMessaging%20API%20Environments%5D=W3siZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X2lkIiwidmFsdWUiOiIiLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiY2xpZW50X3NlY3JldCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6ImFjY2Vzc190b2tlbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Imhvc3QiLCJ2YWx1ZSI6InRhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoiQXV0aG9yaXphdGlvbiIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifSx7ImVuYWJsZWQiOnRydWUsImtleSI6Im9hdXRoX2hvc3QiLCJ2YWx1ZSI6InNhcGkudGVsc3RyYS5jb20iLCJ0eXBlIjoidGV4dCJ9LHsiZW5hYmxlZCI6dHJ1ZSwia2V5IjoibWVzc2FnZV9pZCIsInZhbHVlIjoiIiwidHlwZSI6InRleHQifV0=\">   <img src=\"https://run.pstmn.io/button.svg\" alt=\"Run in Postman\" /></a></p>    <h2>Sample Apps</h2>   - <a href=\"https://github.com/telstra/MessagingAPI-perl-sample-app\">Perl Sample App</a>   - <a href=\"https://github.com/telstra/messaging-sample-code-happy-chat\">Happy Chat App</a>   - <a href=\"https://github.com/developersteve/telstra-messaging-php\">PHP Sample App</a>    <h2>SDK repos</h2>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-php\">Messaging API - PHP SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-python\">Messaging API - Python SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-ruby\">Messaging API - Ruby SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-node\">Messaging API - NodeJS SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-dotnet\">Messaging API - .Net2 SDK</a>   - <a href=\"https://github.com/telstra/MessagingAPI-SDK-Java\">Messaging API - Java SDK</a>  # Delivery Notification  The API provides several methods for notifying when a message has been delivered to the destination.  <ol>   <li>When you provision a number there is an opportunity to specify a <code>notifyURL</code>, when the message has been delivered the API will make a call to this URL to advise of the message status. If this is not provided then you can make use the Get Replies API to poll for messages.</li>   <li>If you do not specify a URL you can always call the <code>GET /sms</code> API get the latest replies to the message.</li> </ol>  <I>Please note that the notification URLs and the polling call are exclusive. If a notification URL has been set then the polling call will not provide any useful information.</I>  <h2>Notification URL Format</h2>  When a message has reached its final state, the API will send a POST to the URL that has been previously specified.   <h3>Notification URL Format for SMS</h3> <pre><code class=\"language-sh\">{     to: '+61418123456'     sentTimestamp: '2017-03-17T10:05:22+10:00'     receivedTimestamp: '2017-03-17T10:05:23+10:00'     messageId: /cccb284200035236000000000ee9d074019e0301/1261418123456     deliveryStatus: DELIVRD   } </code></pre> \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>to</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>deliveryStatus</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>messageId</code></td>       <td>The same reference that was returned when the original message was sent.</td>     </tr>     <tr>       <td><code>receivedTimestamp</code></td>       <td>Time the message was sent to the API.</td>     </tr>   </tbody> </table>  Upon receiving this call it is expected that your servers will give a 204 (No Content) response. Anything else will cause the API to reattempt the call 5 minutes later.   <h3>Notification URL Format for SMS Replies</h3> <pre><code class=\"language-sh\">{     \"status\": \"RECEIVED\"     \"destinationAddress\": \"+61418123456\"     \"senderAddress\": \"+61421987654\"     \"message\": \"Foo\"             \"sentTimestamp\": \"2018-03-23T12:10:06+10:00\"   }                              </code></pre>  \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>status</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>destinationAddress</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>senderAddress</code></td>       <td>The number the message was sent from.</td>     </tr>     <tr>       <td><code>message</code></td>       <td>The sontent of the SMS reply.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>   </tbody> </table>  <h3>Notification URL Format for MMS Replies</h3> <pre><code class=\"language-sh\">{     \"status\": \"RECEIVED\",     \"destinationAddress\": \"+61418123456\",     \"senderAddress\": \"+61421987654\",     \"subject\": \"Foo\",     \"sentTimestamp\": \"2018-03-23T12:15:45+10:00\",     \"envelope\": \"string\",     \"MMSContent\":      [       {         \"type\": \"application/smil\",         \"filename\": \"smil.xml\",         \"payload\": \"string\"       },        {         \"type\": \"image/jpeg\",         \"filename\": \"sample.jpeg\",         \"payload\": \"string\"        }      ]    } </code></pre>  \\ The fields are:  <table>   <thead>     <tr>       <th>Field</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>status</code></td>       <td>The final state of the message.</td>     </tr>     <tr>       <td><code>destinationAddress</code></td>       <td>The number the message was sent to.</td>     </tr>     <tr>       <td><code>senderAddress</code></td>       <td>The number the message was sent from.</td>     </tr>     <tr>       <td><code>subject</code></td>       <td>The subject assigned to the message.</td>     </tr>     <tr>       <td><code>sentTimestamp</code></td>       <td>Time handling of the message ended.</td>     </tr>     <tr>       <td><code>envelope</code></td>       <td>Information about about terminal type and originating operator.</td>     </tr>     <tr>       <td><code>MMSContent</code></td>       <td>An array of the actual content of the reply message.</td>     </tr>     <tr>       <td><code>type</code></td>       <td>The content type of the message.</td>     </tr>     <tr>       <td><code>filename</code></td>       <td>The filename for the message content.</td>     </tr>     <tr>       <td><code>payload</code></td>       <td>The content of the message.</td>     </tr>   </tbody> </table>  # Frequently Asked Questions **Q: Can I send a broadcast message using the Telstra Messging API?** A. Yes. Recipient numbers can be in teh form of an array of strings if a broadcast message needs to be sent.  <h2>Notes</h2> <a href=\"http://petstore.swagger.io/?url=https://raw.githubusercontent.com/telstra/MessagingAPI-v2/master/docs/swagger/messaging-api-swagger.yaml\" target=\"_blank\">View messaging in Swagger UI</a>  # noqa: E501

    OpenAPI spec version: 2.2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import copy
import logging
import multiprocessing
import sys
import urllib3

import six
from six.moves import http_client as httplib


class TypeWithDefault(type):
    def __init__(cls, name, bases, dct):
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls):
        if cls._default is None:
            cls._default = type.__call__(cls)
        return copy.copy(cls._default)

    def set_default(cls, default):
        cls._default = copy.copy(default)


class Configuration(six.with_metaclass(TypeWithDefault, object)):
    """NOTE: This class is auto generated by the swagger code generator program.

    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    def __init__(self):
        """Constructor"""
        # Default Base url
        self.host = "https://tapi.telstra.com/v2"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""

        # access token for OAuth
        self.access_token = ""

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("Telstra_Messaging")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if (self.api_key.get(identifier) and
                self.api_key_prefix.get(identifier)):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]  # noqa: E501
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(
            basic_auth=self.username + ':' + self.password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {

            'auth':
                {
                    'type': 'oauth2',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': 'Bearer ' + self.access_token
                },

        }

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 2.2.6\n"\
               "SDK Package Version: 1.0.4".\
               format(env=sys.platform, pyversion=sys.version)
