#####################################################
#   Function App (Consumption Plan)
#####################################################
# In this case, we assume that the resource group "getresumevisitorcounter" already exists, as I created it.
# If you have NOT already created the resource group "getresumevisitorcounter",
# remove this comment and optionally define it here. For example:
#
# resource "azurerm_resource_group" "rg_function" {
#   name     = "getresumevisitorcounter"
#   location = var.location
# }
#

# App Service Plan for the Function
resource "azurerm_app_service_plan" "function_plan" {
  name                = "ASP-GetResumeVisitorCounter-5523"
  resource_group_name = "getresumevisitorcounter"  # <--- existing RG
  location            = "germanywestcentral"
  os_type            = "Linux"
  sku_name           = "Y1"
  #kind                = "functionapp"

  sku {
    tier = "Dynamic"
    size = "Y1"
  }
}

# Storage Account for the Function App
resource "azurerm_storage_account" "function_storage" {
  name                     = var.func_storage_account_name
  resource_group_name      = azurerm_resource_group.rg_function.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  kind                     = "StorageV2"
}

# Main Function App resource (Python 3.11 on Linux, Consumption Plan)
resource "azurerm_function_app" "function_app" {
  name                       = var.function_app_name
  resource_group_name        = azurerm_resource_group.rg_function.name
  location                   = var.location
  app_service_plan_id        = azurerm_app_service_plan.function_plan.id
  storage_account_name       = azurerm_storage_account.function_storage.name
  storage_account_access_key = azurerm_storage_account.function_storage.primary_access_key
  os_type                    = "linux"
  functions_version          = 4

  site_config {
    linux_fx_version = "Python|3.11"
  }

  # Basic environment variables
  # We'll merge Cosmos DB variables in cosmos_db.tf via a second resource
  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME" = "python"
    "WEBSITE_RUN_FROM_PACKAGE" = "1"
    # Provide AzureWebJobsStorage so Functions can run
    "AzureWebJobsStorage"      = azurerm_storage_account.function_storage.primary_connection_string
  }
}