#####################################################
#   Storage Account (Static Website) + CDN
#####################################################

resource "azurerm_storage_account" "static_site_storage" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.rg_storage_cdn.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  kind                     = "StorageV2"
  allow_nested_items_to_be_public = true
  #allow_blob_public_access = true

  static_website {
    index_document     = "index.html"
    error_404_document = "404.html"
  }
}

resource "azurerm_cdn_profile" "cdn_profile" {
  name                = var.cdn_profile_name
  resource_group_name = azurerm_resource_group.rg_storage_cdn.name
  location            = var.location
  sku                 = "Standard_Microsoft" 
  # or "Standard_Verizon", "Premium_Verizon", etc.
}

resource "azurerm_cdn_endpoint" "cdn_endpoint" {
  name                = var.cdn_endpoint_name
  profile_name        = azurerm_cdn_profile.cdn_profile.name
  resource_group_name = azurerm_resource_group.rg_storage_cdn.name
  location            = var.location

  is_http_allowed    = false
  is_https_allowed   = true
  origin_host_header = azurerm_storage_account.static_site_storage.primary_web_host
  origin_path        = "$web"

  origin {
    name      = "staticSiteStorageOrigin"
    host_name = azurerm_storage_account.static_site_storage.primary_web_host
  }
}
