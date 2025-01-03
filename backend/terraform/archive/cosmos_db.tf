#####################################################
#   Cosmos DB: Account, SQL DB, Container
#####################################################

resource "azurerm_cosmosdb_account" "db_acct" {
  name                = var.cosmos_db_account_name
  resource_group_name = azurerm_resource_group.rg_cosmos.name
  location            = "westeurope" # or "West Europe"
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level       = "Session"
    max_interval_in_seconds = 5
    max_staleness_prefix    = 100
  }

  geo_location {
    location          = "westeurope" # or "West Europe"
    failover_priority = 0
  }

  backup {
    type = "Continuous"
  }
}

resource "azurerm_cosmosdb_sql_database" "db_sql" {
  name                = var.cosmos_db_name
  resource_group_name = azurerm_resource_group.rg_cosmos.name
  account_name        = azurerm_cosmosdb_account.db_acct.name
}

resource "azurerm_cosmosdb_sql_container" "db_container" {
  name                = var.cosmos_db_container_name
  resource_group_name = azurerm_resource_group.rg_cosmos.name
  account_name        = azurerm_cosmosdb_account.db_acct.name
  database_name       = azurerm_cosmosdb_sql_database.db_sql.name
  partition_key_path  = "/id"
  throughput          = 400
}

# We can set or update function app settings to reference these Cosmos values
resource "azurerm_function_app" "function_app_settings" {
  name                = azurerm_function_app.function_app.name
  resource_group_name = azurerm_function_app.function_app.resource_group_name
  location            = azurerm_function_app.function_app.location

  app_service_plan_id        = azurerm_function_app.function_app.app_service_plan_id
  storage_account_name       = azurerm_function_app.function_app.storage_account_name
  storage_account_access_key = azurerm_function_app.function_app.storage_account_access_key
  os_type                    = azurerm_function_app.function_app.os_type
  functions_version          = azurerm_function_app.function_app.functions_version

  # Inherit existing site_config and add new or updated app_settings
  site_config {
    linux_fx_version = azurerm_function_app.function_app.site_config.0.linux_fx_version
  }

  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME" = "python"
    "WEBSITE_RUN_FROM_PACKAGE" = "1"

    # Cosmos DB references
    "COSMOS_DB_ACCOUNT_URI" = azurerm_cosmosdb_account.db_acct.endpoint
    "COSMOS_DB_ACCOUNT_KEY" = azurerm_cosmosdb_account.db_acct.primary_master_key
    "COSMOS_DB_NAME"        = azurerm_cosmosdb_sql_database.db_sql.name
    "COSMOS_DB_CONTAINER"   = azurerm_cosmosdb_sql_container.db_container.name

    # Additional environment variables if needed
    "AzureWebJobsStorage"   = azurerm_storage_account.function_storage.primary_connection_string
  }

  # This ensures Terraform updates the function app, rather than replacing it
  depends_on = [
    azurerm_function_app.function_app,
    azurerm_cosmosdb_sql_container.db_container
  ]
}
