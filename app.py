from telstramessagingapi.telstramessagingapi_client import TelstramessagingapiClient
from telstramessagingapi.models.o_auth_scope_enum import OAuthScopeEnum
from telstramessagingapi.exceptions.o_auth_provider_exception import OAuthProviderException
from var_dump import var_dump

o_auth_client_id = 'wRMg7VIlpgDq1OHEyrtTB9mdHREehLIe' # OAuth 2 Client ID
o_auth_client_secret = 'jc6EkPBAHoTAvBoR' # OAuth 2 Client Secret

client = TelstramessagingapiClient(o_auth_client_id, o_auth_client_secret)

token = client.auth.authorize([OAuthScopeEnum.NSMS])

provisioning_client = client.provisioning

result = provisioning_client.get_subscription()

var_dump(result)
