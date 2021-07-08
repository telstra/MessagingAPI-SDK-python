"""Tests for the configuration."""

import pytest

from telstra.messaging import exceptions
from telstra.messaging.utils import config

GET_ERROR_TESTS = [
    pytest.param(
        "TELSTRA_CLIENT_ID",
        "telstra_client_id",
        exceptions.CredentialError,
        [
            "client id",
            "https://dev.telstra.com/user/me/apps",
        ],
        id="TELSTRA_CLIENT_ID",
    ),
    pytest.param(
        "TELSTRA_CLIENT_SECRET",
        "telstra_client_secret",
        exceptions.CredentialError,
        [
            "client secret",
            "https://dev.telstra.com/user/me/apps",
        ],
        id="TELSTRA_CLIENT_SECRET",
    ),
]


@pytest.mark.parametrize(
    "env_name, config_name, expected_exception, expected_contents", GET_ERROR_TESTS
)
@pytest.mark.config
def test_get_error(
    env_name, config_name, expected_exception, expected_contents, monkeypatch
):
    """
    GIVEN environment variable name, configuration name and expected exception and
        contents
    WHEN the environment variable is deleted and the config retrieved
    THEN the expected exception is raised with the expected contents.
    """
    monkeypatch.delenv(env_name)

    with pytest.raises(expected_exception) as exc_info:
        getattr(config.Config(), config_name)

    for content in expected_contents:
        assert content in str(exc_info.value)


GET_ENV_DEFINED_TESTS = [
    pytest.param(
        "TELSTRA_CLIENT_ID",
        "telstra_client_id",
        "client id 1",
        id="TELSTRA_CLIENT_ID",
    ),
    pytest.param(
        "TELSTRA_CLIENT_SECRET",
        "telstra_client_secret",
        "client secret 1",
        id="TELSTRA_CLIENT_SECRET",
    ),
]


@pytest.mark.parametrize("env_name, config_name, env_value", GET_ENV_DEFINED_TESTS)
@pytest.mark.config
def test_get_env_defined(env_name, config_name, env_value, monkeypatch):
    """
    GIVEN environment variable name and value and configuration name
    WHEN the environment variable is set and the config retrieved
    THEN value from the environment is returned.
    """
    monkeypatch.setenv(env_name, env_value)

    returned_value = getattr(config.Config(), config_name)

    assert returned_value == env_value


GET_CONFIG_SET_TESTS_TESTS = [
    pytest.param("telstra_client_id", "client id 1", id="telstra_client_id"),
    pytest.param(
        "telstra_client_secret", "client secret 1", id="telstra_client_secret"
    ),
]


@pytest.mark.parametrize("config_name, config_value", GET_CONFIG_SET_TESTS_TESTS)
@pytest.mark.config
def test_get_config_set(config_name, config_value):
    """
    GIVEN configuration name and value
    WHEN the config is set is set and then retrieved
    THEN value is returned.
    """
    config_instance = config.Config()
    setattr(config_instance, config_name, config_value)

    returned_value = getattr(config_instance, config_name)

    assert returned_value == config_value


@pytest.mark.parametrize("config_name, config_value", GET_CONFIG_SET_TESTS_TESTS)
@pytest.mark.config
def test_init_config_set(config_name, config_value):
    """
    GIVEN configuration name and value
    WHEN the config is constructed with the value and then retrieved
    THEN value is returned.
    """
    config_instance = config.Config(**{config_name: config_value})

    returned_value = getattr(config_instance, config_name)

    assert returned_value == config_value


SET_ERROR_TESTS = [
    pytest.param(
        "telstra_client_id",
        True,
        exceptions.CredentialError,
        [str(True), "str"],
        id="telstra_client_id",
    ),
    pytest.param(
        "telstra_client_secret",
        True,
        exceptions.CredentialError,
        [str(True), "str"],
        id="telstra_client_secret",
    ),
]


@pytest.mark.parametrize(
    "config_name, config_value, expected_exception, expected_contents", SET_ERROR_TESTS
)
@pytest.mark.config
def test_set_error(config_name, config_value, expected_exception, expected_contents):
    """
    GIVEN configuration name and value and expected exception and contents
    WHEN the configuration is set
    THEN the expected exception is raised with the expected contents.
    """
    with pytest.raises(expected_exception) as exc_info:
        setattr(config.Config(), config_name, config_value)

    for content in expected_contents:
        assert content in str(exc_info.value)


@pytest.mark.parametrize(
    "config_name, config_value, expected_exception, expected_contents", SET_ERROR_TESTS
)
@pytest.mark.config
def test_constructed_error(
    config_name, config_value, expected_exception, expected_contents
):
    """
    GIVEN configuration name and value and expected exception and contents
    WHEN the configuration is constructed
    THEN the expected exception is raised with the expected contents.
    """
    with pytest.raises(expected_exception) as exc_info:
        config.Config(**{config_name: config_value})

    for content in expected_contents:
        assert content in str(exc_info.value)
