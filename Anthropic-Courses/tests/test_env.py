import os
import subprocess
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from common.env import load_environment_variables

subprocess.run("clear", shell=True)  # Clear the terminal for better readability of test output

def test_read_prod_githubname():
    load_environment_variables()
    assert os.getenv("GITHUB_NAME") == "sunitghub"
    print(f"\nGITHUB_NAME is {os.getenv('GITHUB_NAME')}.")


def test_load_environment_variables_success():
    """Test that load_environment_variables finds and loads .env"""
    with tempfile.TemporaryDirectory() as tmpdir:
        env_file = Path(tmpdir) / ".env"
        env_file.write_text("TEST_VAR=hello\n")
        
        with patch('common.env.find_dotenv', return_value=str(env_file)):
            result = load_environment_variables()
            assert result == Path(tmpdir)
            assert os.getenv("TEST_VAR") == "hello"

def test_load_environment_variables_not_found(capsys):
    """Test that graceful error when .env not found"""
    with patch('common.env.find_dotenv', return_value=None):
        result = load_environment_variables()
        assert result is None
        captured = capsys.readouterr()
        assert "No .env file found" in captured.out

def test_returns_parent_directory():
    """Test that function returns the parent directory of .env"""
    with tempfile.TemporaryDirectory() as tmpdir:
        env_file = Path(tmpdir) / ".env"
        env_file.write_text("VAR=value\n")
        
        with patch('common.env.find_dotenv', return_value=str(env_file)):
            root = load_environment_variables()
            assert root == Path(tmpdir)