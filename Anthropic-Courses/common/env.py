from pathlib import Path

try:
    from dotenv import load_dotenv, find_dotenv

    def _candidate_dotenv_paths():
        """Yield likely .env locations, ordered from most to least specific."""
        seen = set()
        starts = [Path.cwd(), Path(__file__).resolve().parent]
        for start in starts:
            for directory in (start, *start.parents):
                if directory in seen:
                    continue
                seen.add(directory)
                yield directory / ".env"

    def load_environment_variables():
        found = find_dotenv(usecwd=True)
        if not found:
            found = next((str(path) for path in _candidate_dotenv_paths() if path.is_file()), None)
        if not found:
            print("No .env file found. Please create one with your environment variables.")
            return None
        dotenv_path = Path(found)
        load_dotenv(dotenv_path)
        return dotenv_path.parent
except ImportError as e:
    print(f"Error importing dotenv: {e}")
