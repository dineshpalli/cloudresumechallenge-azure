#####################################################
#   Resource Groups
#####################################################

# 1. For Storage & CDN
resource "azurerm_resource_group" "rg_storage_cdn" {
  name     = var.rg_storage_cdn_name
  location = var.location
}

# 2. For Function App 
resource "azurerm_resource_group" "rg_function" {
  name     = var.rg_function_name
  location = var.location
}

# 3. For Cosmos DB (cloudresumechallengeAPI)
resource "azurerm_resource_group" "rg_cosmos" {
  name     = "cloudresumechallengeAPI"
  location = "West Europe"
}
