import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.api.function_app import get_visitor_count
from azure.cosmos import CosmosClient


def load_local_settings():
    settings_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../api/local.settings.json")
    )
    with open(settings_path, "r") as f:
        config = json.load(f)

    for key, value in config["Values"].items():
        os.environ[key] = value


load_local_settings()

# Define the azure cosmos db connection details as global variables
endpoint = os.environ["COSMOS_DB_ACCOUNT_URI"]
account_key = os.environ["COSMOS_DB_ACCOUNT_KEY"]
database_name = os.environ["COSMOS_DB_NAME"]
container_name = os.environ["COSMOS_DB_CONTAINER"]

client = CosmosClient(url=endpoint, credential=account_key)
item_id = "1"

database = client.get_database_client(database_name)
container = database.get_container_client(container_name)


def get_count_from_cosmosdb() -> int:

    count_item = container.read_item(item_id, item_id)
    current_count = count_item.get("count", 0)
    return current_count


def test_resume_counter():
    initial_count = get_count_from_cosmosdb()

    # increment_count in cosmos db with a new API call
    req = requests.get(
        "https://getresumevisitorcounter.azurewebsites.net/api/http_trigger_py"
    )
    get_visitor_count(req)

    new_count = get_count_from_cosmosdb()

    # if new_count is greater than intial_count then our test passed
    print(f"Initial Count: {initial_count} | New Count: {new_count}")
    assert new_count > initial_count
