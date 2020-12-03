"""Tests for the environment """

import os

import pytest

from messaging.utils import environment
from messaging import exceptions


class TestReadEnvironment:
    """Tests for _read_environment."""

    # pylint: disable=protected-access

    @staticmethod
    def test_no_client_id(monkeypatch):
        """
        GIVEN environment without CLIENT_ID
        WHEN _read_environment is called
        THEN CredentialError is raised.
        """
        monkeypatch.delenv("CLIENT_ID", raising=False)

        with pytest.raises(exceptions.CredentialError) as exc:
            environment._read_environment()

        assert "CLIENT_ID" in str(exc)

    @staticmethod
    def test_no_client_secret(monkeypatch):
        """
        GIVEN environment without CLIENT_SECRET
        WHEN _read_environment is called
        THEN CredentialError is raised.
        """
        monkeypatch.delenv("CLIENT_SECRET", raising=False)

        with pytest.raises(exceptions.CredentialError) as exc:
            environment._read_environment()

        assert "CLIENT_SECRET" in str(exc)

    @staticmethod
    def test_client_id_secret_defined():
        """
        GIVEN environment with CLIENT_ID and CLIENT_SECRET
        WHEN _read_environment is called
        THEN the CLIENT_ID and CLIENT_SECRET are returned.
        """
        returned_environment = environment._read_environment()

        assert returned_environment.client_id == os.getenv("CLIENT_ID")
        assert returned_environment.client_secret == os.getenv("CLIENT_SECRET")


def test_get(monkeypatch):
    """
    GIVEN environment with CLIENT_ID and CLIENT_SECRET
    WHEN get is called
    THEN the CLIENT_ID and CLIENT_SECRET are returned.
    """
    returned_environment = environment.get()

    assert returned_environment.client_id == os.getenv("CLIENT_ID")
    assert returned_environment.client_secret == os.getenv("CLIENT_SECRET")
