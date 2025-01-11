import sys
import json
import azure.functions as func
import logging
import os
from azure.cosmos import CosmosClient, PartitionKey

# Initialize Azure Function with function-level authentication
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


def _get_cosmos_container():
    """
    Lazily load Cosmos DB connection details and client.
    This function checks environment variables at runtime
    (rather than at module import time).
    """
    required_env_vars = [
        "COSMOS_DB_ACCOUNT_URI",
        "COSMOS_DB_ACCOUNT_KEY",
        "COSMOS_DB_NAME",
        "COSMOS_DB_CONTAINER",
    ]

    # Check for any missing environment variables.
    missing_vars = [var for var in required_env_vars if var not in os.environ]
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )

    # Extract Cosmos DB connection details from environment variables.
    cosmos_db_uri = os.environ["COSMOS_DB_ACCOUNT_URI"]
    cosmos_db_key = os.environ["COSMOS_DB_ACCOUNT_KEY"]
    cosmos_db_name = os.environ["COSMOS_DB_NAME"]
    cosmos_db_container = os.environ["COSMOS_DB_CONTAINER"]

    # Set up the Cosmos DB client and container.
    client = CosmosClient(cosmos_db_uri, credential=cosmos_db_key)
    database = client.get_database_client(cosmos_db_name)
    container = database.get_container_client(cosmos_db_container)

    return container


# HTTP trigger function that increments and returns the visitor count
@app.route(route="http_trigger_py")
def get_visitor_count(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing getVisitorCount request. Kindly wait...")

    try:
        # Initialize Cosmos container on-demand (includes env var checks)
        container = _get_cosmos_container()

        # Try to fetch the existing count document with id="1"
        item = None
        try:
            item = container.read_item(item="1", partition_key="1")
            logging.debug(f"Found item: {item}, the existing count document.")
        except Exception as e:
            # If document doesn't exist, initialize with count=42
            # 42 is used as a fun reference to "Hitchhiker's Guide to the Galaxy"
            logging.error(f"The count document not found or an error occurred: {e}")
            item = {"id": "1", "count": 42}

        # Get current count, defaulting to 42 if not found
        current_count = item.get("count", 42)

        # Ensure count is a valid integer; if corrupted, reset to 42
        if not isinstance(current_count, int):
            logging.error(
                f"Current count is invalid. Resetting to 42! "
                f"(Why 42 you ask? It's a galactic inside joke. "
                f"Grab a towel and go figure it out). Item: {item}"
            )
            current_count = 42

        # Increment the visitor count
        new_count = current_count + 1
        item["count"] = new_count

        # Save updated count back to Cosmos DB
        container.upsert_item(item)
        logging.info(f"Updated visitor count to {new_count}")

        # Return new count as JSON response
        response_body = {"count": new_count}
        return func.HttpResponse(
            body=json.dumps(response_body),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        # Handle any unexpected errors
        logging.error(f"Error updating visitor count: {e}", exc_info=True)
        error_body = {"error": "Unable to retrieve and update visitor count."}
        return func.HttpResponse(
            body=json.dumps(error_body),
            status_code=500,
            mimetype="application/json",
        )
