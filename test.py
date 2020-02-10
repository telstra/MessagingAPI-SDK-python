from __future__ import print_function
import time, os
from pprint import pprint
Telstra_Messaging = __import__('Telstra_Messaging')

from Telstra_Messaging.api.authentication_api import AuthenticationApi
from Telstra_Messaging.rest import ApiException

configuration = Telstra_Messaging.Configuration()
api_instance = Telstra_Messaging.AuthenticationApi(Telstra_Messaging.ApiClient(configuration))
client_id = os.environ.get('CLIENT_ID') # str | 
client_secret = os.environ.get('CLIENT_SECRET') # str | 
grant_type = "client_credentials" # str |  (default to "client_credentials")

try:
    # Generate OAuth2 token
    api_response = api_instance.auth_token(client_id, client_secret, grant_type)
    pprint(api_response)

    configuration.access_token = api_response.access_token

    api_instance = Telstra_Messaging.ProvisioningApi(Telstra_Messaging.ApiClient(configuration))
    provision_number_request = Telstra_Messaging.ProvisionNumberRequest(90)

    api_response = api_instance.create_subscription(provision_number_request)
    pprint(api_response)

    api_instance = Telstra_Messaging.MessagingApi(Telstra_Messaging.ApiClient(configuration))

    send_sms_request = Telstra_Messaging.SendSMSRequest(os.environ.get('PHONE_NO'), "Test the Python SDK code", os.environ.get('FROM_ALIAS'))
    
    api_response = api_instance.send_sms(send_sms_request)
    pprint(api_response)

except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_token: %s\n" % e)