"""Tests for the environment """

import os

import pytest

from messaging.utils import environment
from messaging import exceptions


class TestReadEnvironment:
    """Tests for _read_environment."""

    # pylint: disable=protected-access

    @staticmethod
    def test_no_tls_client_key(monkeypatch):
        """
        GIVEN environment without TLS_CLIENT_KEY
        WHEN _read_environment is called
        THEN CredentialError is raised.
        """
        monkeypatch.delenv("TLS_CLIENT_KEY", raising=False)

        with pytest.raises(exceptions.CredentialError) as exc:
            environment._read_environment()

        assert "TLS_CLIENT_KEY" in str(exc)
        assert "https://dev.telstra.com/user/me/apps" in str(exc)

    @staticmethod
    def test_no_tls_client_secret(monkeypatch):
        """
        GIVEN environment without TLS_CLIENT_SECRET
        WHEN _read_environment is called
        THEN CredentialError is raised.
        """
        monkeypatch.delenv("TLS_CLIENT_SECRET", raising=False)

        with pytest.raises(exceptions.CredentialError) as exc:
            environment._read_environment()

        assert "TLS_CLIENT_SECRET" in str(exc)
        assert "https://dev.telstra.com/user/me/apps" in str(exc)

    @staticmethod
    def test_client_id_secret_defined():
        """
        GIVEN environment with CLIENT_ID and CLIENT_SECRET
        WHEN _read_environment is called
        THEN the CLIENT_ID and CLIENT_SECRET are returned.
        """
        returned_environment = environment._read_environment()

        assert returned_environment.tls_client_key == os.getenv("TLS_CLIENT_KEY")
        assert returned_environment.tls_client_secret == os.getenv("TLS_CLIENT_SECRET")


def test_get(monkeypatch):
    """
    GIVEN environment with TLS_CLIENT_KEY and TLS_CLIENT_SECRET
    WHEN get is called
    THEN the TLS_CLIENT_KEY and TLS_CLIENT_SECRET are returned.
    """
    returned_environment = environment.get()

    assert returned_environment.tls_client_key == os.getenv("TLS_CLIENT_KEY")
    assert returned_environment.tls_client_secret == os.getenv("TLS_CLIENT_SECRET")
