# coding: utf-8

"""
    Telstra Messaging API

    The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages. 
"""


import sys
from setuptools import setup, find_packages

NAME = "Telstra"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["cachecontrol", "jsonpickle", "requests", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Telstra Messaging API",
    author_email="",
    url="https://github.com/telstra/MessagingAPI-SDK-python",
    keywords=["Telstra Messaging SDK - Python Library"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
     The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia&#39;s leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages. 
    """
)
