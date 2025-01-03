#####################################################
#   Outputs
#####################################################

output "static_website_url" {
  description = "Primary endpoint for the static website"
  value       = azurerm_storage_account.static_site_storage.primary_web_endpoint
}

output "cdn_endpoint_host_name" {
  description = "Hostname for the CDN endpoint"
  value       = azurerm_cdn_endpoint.cdn_endpoint.host_name
}

output "function_app_hostname" {
  description = "Default hostname for the Function App"
  value       = azurerm_function_app.function_app.default_hostname
}

output "cosmos_db_endpoint" {
  description = "Cosmos DB endpoint"
  value       = azurerm_cosmosdb_account.db_acct.endpoint
}
