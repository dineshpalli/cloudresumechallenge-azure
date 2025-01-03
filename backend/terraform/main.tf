#####################################################
#   Terraform & AzureRM Provider Configuration
#####################################################
terraform {
  required_version = ">= 1.10.3"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.14.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "b7e0a645-571c-479d-8b11-c96124f8c45d"
}

# Resource Group configuration
resource "azurerm_resource_group" "rg_function" {
  name     = "getresumevisitorcounter"
  location = "germanywestcentral"
}

# Storage Account resource configuration
resource "azurerm_storage_account" "function_storage" {
  name                     = "getresumevisitorcounter"
  resource_group_name      = azurerm_resource_group.rg_function.name
  location                 = azurerm_resource_group.rg_function.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# App Service Plan for the Function (Using azurerm_app_service_plan)
resource "azurerm_app_service_plan" "function_plan" {
  name                = "ASP-GetResumeVisitorCounter-5523"
  resource_group_name = azurerm_resource_group.rg_function.name
  location            = azurerm_resource_group.rg_function.location
  kind                = "FunctionApp"  # Optional but recommended
  reserved            = true           # Indicates Linux OS, false sets to windows

  sku {
    tier = "Dynamic"
    size = "Y1"
  }
}

# Main Function App resource (Python 3.11 on Linux, Consumption Plan)
resource "azurerm_function_app" "function_app" {
  name                       = "GetResumeVisitorCounter"
  resource_group_name        = azurerm_resource_group.rg_function.name
  location                   = azurerm_resource_group.rg_function.location
  app_service_plan_id        = azurerm_app_service_plan.function_plan.id
  storage_account_name       = azurerm_storage_account.function_storage.name
  storage_account_access_key = azurerm_storage_account.function_storage.primary_access_key
  version                    = "~4"
  os_type                    = "linux"

  site_config {
    linux_fx_version = "Python|3.11"
  }
}
