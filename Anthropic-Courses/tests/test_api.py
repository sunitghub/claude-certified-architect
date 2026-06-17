import pytest

from common.env import load_environment_variables

from anthropic import Anthropic

def test_anthropic_client_initialization():
    load_environment_variables()
    client = Anthropic()
    model = "claude-sonnet-4-6"
    assert client is not None