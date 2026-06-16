import os
from pathlib import Path

try:
    from dotenv import load_dotenv, find_dotenv
    def load_environment_variables():
        found = find_dotenv(usecwd=True)
        if not found:
            print("No .env file found. Please create one with your environment variables.")
            return None
        dotenv_path = Path(found)
        load_dotenv(dotenv_path)
        return dotenv_path.parent
except ImportError as e:
    print(f"Error importing dotenv: {e}")