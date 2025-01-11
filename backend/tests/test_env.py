import os

def test_env_vars_loaded():
    assert os.getenv("COSMOS_DB_ACCOUNT_URI"), "No COSMOS_DB_ACCOUNT_URI found"
    assert os.getenv("COSMOS_DB_ACCOUNT_KEY"), "No COSMOS_DB_ACCOUNT_KEY found"
    assert os.getenv("COSMOS_DB_NAME"), "No COSMOS_DB_NAME found"
    assert os.getenv("COSMOS_DB_CONTAINER"), "No COSMOS_DB_CONTAINER found"
