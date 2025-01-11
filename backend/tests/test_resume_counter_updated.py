import pytest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from azure.cosmos import CosmosClient
import requests
import json
from azure.cosmos.exceptions import CosmosHttpResponseError

def load_local_settings():
    """
    Load configuration from local.settings.json file
    This enables tests to run locally without manually setting environment variables
    """
    try:
        settings_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../api/local.settings.json")
        )
        with open(settings_path, "r") as f:
            config = json.load(f)
        for key, value in config["Values"].items():
            os.environ[key] = value
    except FileNotFoundError:
        print("Warning: local.settings.json not found. Ensure environment variables are set manually.")
    except json.JSONDecodeError:
        print("Warning: local.settings.json is not valid JSON. Check file format.")

# Load settings before defining configuration
load_local_settings()

# Configuration for Azure Cosmos DB
# These environment variables should be set in the test environment
# or using a configuration file for local development
COSMOS_CONFIG = {
    "endpoint": os.environ.get("COSMOS_DB_ACCOUNT_URI"),
    "account_key": os.environ.get("COSMOS_DB_ACCOUNT_KEY"),
    "database_name": os.environ.get("COSMOS_DB_NAME"),
    "container_name": os.environ.get("COSMOS_DB_CONTAINER"),
    "api_function_key": os.environ.get("API_FUNCTION_KEY"),
    "item_id": "1",
}


class TestResumeCounter:
    @pytest.fixture
    def cosmos_client(self):
        """
        Creates a CosmosDB client fixture for testing.
        Returns a configured client or raises an error if credentials are missing.
        """
        if not all(COSMOS_CONFIG.values()):
            raise ValueError(
                "Missing required Cosmos DB configuration. Check environment variables."
            )

        client = CosmosClient(
            url=COSMOS_CONFIG["endpoint"], credential=COSMOS_CONFIG["account_key"]
        )
        return client

    @pytest.fixture
    def cosmos_container(self, cosmos_client):
        """
        Returns a container client for the specified database and container.
        """
        database = cosmos_client.get_database_client(COSMOS_CONFIG["database_name"])
        container = database.get_container_client(COSMOS_CONFIG["container_name"])
        return container

    def get_count_from_cosmosdb(self, container) -> int:
        """
        Retrieves the current visitor count from Cosmos DB.
        Handles potential errors and returns 0 if item doesn't exist.
        """
        try:
            count_item = container.read_item(
                item=COSMOS_CONFIG["item_id"],
                partition_key=COSMOS_CONFIG["item_id"],
            )
            return count_item.get("count", 0)
        except CosmosHttpResponseError as e:
            pytest.fail(f"Failed to read count from Cosmos DB: {str(e)}")
            return 0

    @pytest.mark.integration
    def test_resume_counter_integration(self, cosmos_container):
        """
        Integration test for the resume counter.
        Verifies that the counter increments correctly through the API.
        """
        # Import the function to test
        from backend.api.function_app import get_visitor_count

        # Get initial count
        initial_count = self.get_count_from_cosmosdb(cosmos_container)

        # Make API call to increment counter
        api_url = f"https://getresumevisitorcounter.azurewebsites.net/api/http_trigger_py?code={COSMOS_CONFIG['api_function_key']}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            pytest.fail(f"API request failed: {str(e)}")

        # Process the request
        get_visitor_count(response)

        # Get new count and verify increment
        new_count = self.get_count_from_cosmosdb(cosmos_container)
        assert (
            new_count > initial_count
        ), f"Counter did not increment. Initial: {initial_count}, New: {new_count}"

    @pytest.mark.unit
    def test_resume_counter_mock(self):
        """
        Unit test for the resume counter using mocked dependencies.
        Tests the counter logic without making actual API calls.
        """
        # Import the function to test
        from backend.api.function_app import get_visitor_count

        mock_container = MagicMock()
        mock_container.read_item.return_value = {"id": "1", "count": 5}

        with patch("azure.cosmos.CosmosClient") as mock_client:
            mock_client.return_value.get_database_client.return_value.get_container_client.return_value = (
                mock_container
            )

            # Mock the API request
            mock_request = MagicMock()
            mock_request.get.return_value.status_code = 200

            # Test counter increment
            initial_count = self.get_count_from_cosmosdb(mock_container)
            get_visitor_count(mock_request)

            # Verify mock was called correctly
            mock_container.read_item.assert_called_once()
            assert initial_count == 5, "Mock initial count should be 5"


if __name__ == "__main__":
    pytest.main([__file__])
