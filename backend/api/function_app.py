import sys
import json
import azure.functions as func
import logging
import os
from azure.cosmos import CosmosClient, PartitionKey

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Define Environment variables
required_env_vars = [
    "COSMOS_DB_ACCOUNT_URI",
    "COSMOS_DB_ACCOUNT_KEY",
    "COSMOS_DB_NAME",
    "COSMOS_DB_CONTAINER",
]

# Handle missing environment variables
missing_vars = [var for var in required_env_vars if var not in os.environ]
if missing_vars:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing_vars)}"
    )

COSMOS_DB_URI = os.environ["COSMOS_DB_ACCOUNT_URI"]
COSMOS_DB_KEY = os.environ["COSMOS_DB_ACCOUNT_KEY"]
COSMOS_DB_NAME = os.environ["COSMOS_DB_NAME"]
COSMOS_DB_CONTAINER = os.environ["COSMOS_DB_CONTAINER"]

# Initialize the Cosmos DB client
client = CosmosClient(COSMOS_DB_URI, credential=COSMOS_DB_KEY)
database = client.get_database_client(COSMOS_DB_NAME)
container = database.get_container_client(COSMOS_DB_CONTAINER)


# Define the HTTP trigger function
@app.route(route="http_trigger_py")
def get_visitor_count(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing getVisitorCount request. Kindly wait...")
    # Attempt to read and increment the count
    try:
        # Fetch the existing count document
        item = None
        try:
            item = container.read_item(item="1", partition_key="1")
            logging.debug(f"Found item: {item}, the existing count document.")
        except Exception as e:
            logging.error(f"The count document not found or an error occurred: {e}")
            # If the document is not found, create it
            item = {"id": "1", "count": 42}
        current_count = item.get("count", 42)
        # Validate if the current count is a number, fallback to 42 if not
        if not isinstance(current_count, int):
            logging.error(
                f"Current count is invalid. Resetting to 42! (Why 42 you ask? Let's just say it's a galactic inside joke. Grab a towel and go figure it out). Item: {item}"
            )
            current_count = 42
        # Increment the count
        new_count = current_count + 1
        item["count"] = new_count

        # Upsert the updated count document
        container.upsert_item(item)
        logging.info(f"Updated visitor count to {new_count}")

        # Return the JSON response
        response_body = {"count": new_count}
        return func.HttpResponse(
            body=json.dumps(response_body), status_code=200, mimetype="application/json"
        )
    except Exception as e:
        # Catch any unexpected errors and log them
        logging.error(f"Error updating visitor count: {e}", exc_info=True)
        error_body = {"error": "Unable to retrieve and update visitor count."}
        return func.HttpResponse(
            body=json.dumps(error_body), status_code=500, mimetype="application/json"
        )
