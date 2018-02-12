# coding: utf-8

"""
    Telstra Messaging API

     The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages.   # noqa: E501

    OpenAPI spec version: 2.2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from Telstra_Messaging.api_client import ApiClient


class AuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def oauth_token_post(self, o_auth_client_id, o_auth_client_secret, **kwargs):  # noqa: E501
        """AuthGeneratetokenPost  # noqa: E501

        generate auth token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.oauth_token_post(o_auth_client_id, o_auth_client_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str o_auth_client_id:  (required)
        :param str o_auth_client_secret:  (required)
        :return: AuthgeneratetokenpostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.oauth_token_post_with_http_info(o_auth_client_id, o_auth_client_secret, **kwargs)  # noqa: E501
        else:
            (data) = self.oauth_token_post_with_http_info(o_auth_client_id, o_auth_client_secret, **kwargs)  # noqa: E501
            return data

    def oauth_token_post_with_http_info(self, o_auth_client_id, o_auth_client_secret, **kwargs):  # noqa: E501
        """AuthGeneratetokenPost  # noqa: E501

        generate auth token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.oauth_token_post_with_http_info(o_auth_client_id, o_auth_client_secret, async=True)
        >>> result = thread.get()

        :param async bool
        :param str o_auth_client_id:  (required)
        :param str o_auth_client_secret:  (required)
        :return: AuthgeneratetokenpostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['o_auth_client_id', 'o_auth_client_secret']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_token_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'o_auth_client_id' is set
        if ('o_auth_client_id' not in params or
                params['o_auth_client_id'] is None):
            raise ValueError("Missing the required parameter `o_auth_client_id` when calling `oauth_token_post`")  # noqa: E501
        # verify the required parameter 'o_auth_client_secret' is set
        if ('o_auth_client_secret' not in params or
                params['o_auth_client_secret'] is None):
            raise ValueError("Missing the required parameter `o_auth_client_secret` when calling `oauth_token_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'o_auth_client_id' in params:
            form_params.append(('oAuthClientId', params['o_auth_client_id']))  # noqa: E501
        if 'o_auth_client_secret' in params:
            form_params.append(('oAuthClientSecret', params['o_auth_client_secret']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/oauth/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthgeneratetokenpostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
