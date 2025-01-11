import os
import json
import pytest

@pytest.fixture(scope="session", autouse=True)
def load_local_settings():
    try:
        with open('backend/api/local.settings.json', 'r') as f:
            settings = json.load(f)
        # Suppose the format is "Values": { "COSMOS_DB_ACCOUNT_URI": "...", ...}
        values = settings.get('Values', {})
        for key, val in values.items():
            os.environ[key] = val
    except FileNotFoundError:
        # If local.settings.json doesn't exist, skip or ignore
        pass 