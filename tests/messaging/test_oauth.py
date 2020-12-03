"""Tests for oauth."""

import pytest

from messaging import oauth, exceptions
from messaging.utils import environment


def test_get_token_success(_valid_credentials):
    """
    GIVEN mocked environment that returns valid credentials
    WHEN get_token is called
    THEN the token is returned.
    """
    token = oauth.get_token()

    assert not token.expired


def test_get_token():
    """
    GIVEN environment with invalid credentials
    WHEN get_token is called
    THEN CredentialError is raised.
    """
    with pytest.raises(exceptions.CredentialError) as exc:
        oauth.get_token()

    assert "Unauthorized" in str(exc)
