import sys
import json
import azure.functions as func
import logging
import os
from azure.cosmos import CosmosClient, PartitionKey

# Initialize Azure Function with function-level authentication
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Required environment variables for Cosmos DB connection
# I need these to connect to and interact with the database
required_env_vars = [
    "COSMOS_DB_ACCOUNT_URI",
    "COSMOS_DB_ACCOUNT_KEY",
    "COSMOS_DB_NAME",
    "COSMOS_DB_CONTAINER",
]

# Check if any required environment variables are missing
# This helps catch configuration issues early
missing_vars = [var for var in required_env_vars if var not in os.environ]
if missing_vars:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing_vars)}"
    )

# Extract Cosmos DB connection details from environment variables
COSMOS_DB_URI = os.environ["COSMOS_DB_ACCOUNT_URI"]
COSMOS_DB_KEY = os.environ["COSMOS_DB_ACCOUNT_KEY"]
COSMOS_DB_NAME = os.environ["COSMOS_DB_NAME"]
COSMOS_DB_CONTAINER = os.environ["COSMOS_DB_CONTAINER"]

# Set up connection to Cosmos DB
# This creates reusable clients that persist across function invocations
client = CosmosClient(COSMOS_DB_URI, credential=COSMOS_DB_KEY)
database = client.get_database_client(COSMOS_DB_NAME)
container = database.get_container_client(COSMOS_DB_CONTAINER)


# HTTP trigger function that increments and returns the visitor count
@app.route(route="http_trigger_py")
def get_visitor_count(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing getVisitorCount request. Kindly wait...")
    
    try:
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
        
        # Ensure count is a valid integer
        # If corrupted, reset to 42 as fallback
        if not isinstance(current_count, int):
            logging.error(
                f"Current count is invalid. Resetting to 42! (Why 42 you ask? Let's just say it's a galactic inside joke. Grab a towel and go figure it out). Item: {item}"
            )
            current_count = 42

        # Increment the visitor count
        new_count = current_count + 1
        item["count"] = new_count

        # Save updated count back to database
        container.upsert_item(item)
        logging.info(f"Updated visitor count to {new_count}")

        # Return new count as JSON response
        response_body = {"count": new_count}
        return func.HttpResponse(
            body=json.dumps(response_body), status_code=200, mimetype="application/json"
        )

    except Exception as e:
        # Handle any unexpected errors
        logging.error(f"Error updating visitor count: {e}", exc_info=True)
        error_body = {"error": "Unable to retrieve and update visitor count."}
        return func.HttpResponse(
            body=json.dumps(error_body), status_code=500, mimetype="application/json"
        )